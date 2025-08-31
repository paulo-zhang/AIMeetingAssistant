"""
Audio Capture Module

Handles real-time audio capture from microphone input.
"""

import pyaudio
import numpy as np
import sounddevice as sd
from typing import Callable, Optional
import threading
import queue
import time
from loguru import logger

class AudioCapture:
    """Real-time audio capture from microphone"""
    
    def __init__(self, sample_rate=16000, channels=1, chunk_size=1024):
        self.sample_rate = sample_rate
        self.channels = channels
        self.chunk_size = chunk_size
        self.audio_queue = queue.Queue()
        self.is_recording = False
        self.audio_thread = None
        self.pyaudio_instance = None
        
    def start_capture(self, callback: Optional[Callable] = None):
        """Start real-time audio capture"""
        if self.is_recording:
            logger.warning("Audio capture already running")
            return
            
        self.is_recording = True
        self.audio_thread = threading.Thread(
            target=self._capture_audio,
            args=(callback,)
        )
        self.audio_thread.start()
        logger.info("Audio capture started")
        
    def _capture_audio(self, callback):
        """Internal audio capture loop using sounddevice"""
        try:
            with sd.InputStream(
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype=np.float32,
                blocksize=self.chunk_size,
                callback=self._audio_callback
            ):
                while self.is_recording:
                    if not self.audio_queue.empty():
                        audio_data = self.audio_queue.get()
                        if callback:
                            callback(audio_data)
                    time.sleep(0.01)  # Small delay to prevent busy waiting
        except Exception as e:
            logger.error(f"Audio capture error: {e}")
            self.is_recording = False
                        
    def _audio_callback(self, indata, frames, time, status):
        """Callback for audio input"""
        if status:
            logger.warning(f"Audio status: {status}")
        self.audio_queue.put(indata.copy())
        
    def stop_capture(self):
        """Stop audio capture"""
        self.is_recording = False
        if self.audio_thread:
            self.audio_thread.join()
        logger.info("Audio capture stopped")
        
    def get_audio_data(self) -> Optional[np.ndarray]:
        """Get the latest audio data from the queue"""
        if not self.audio_queue.empty():
            return self.audio_queue.get()
        return None
        
    def is_speaking(self, audio_data: np.ndarray, threshold=0.01) -> bool:
        """Detect if audio contains speech"""
        if audio_data is None or len(audio_data) == 0:
            return False
        energy = np.mean(audio_data ** 2)
        return energy > threshold
