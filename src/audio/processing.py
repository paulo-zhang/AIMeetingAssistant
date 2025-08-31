"""
Audio Processing Module

Handles audio preprocessing, noise reduction, and signal enhancement.
"""

import numpy as np
import librosa
from scipy import signal
from typing import Optional
from loguru import logger

class AudioProcessor:
    """Audio preprocessing and enhancement"""
    
    def __init__(self, sample_rate=16000):
        self.sample_rate = sample_rate
        
    def normalize_audio(self, audio: np.ndarray) -> np.ndarray:
        """Normalize audio to [-1, 1] range"""
        if len(audio) == 0:
            return audio
            
        max_val = np.max(np.abs(audio))
        if max_val > 0:
            return audio / max_val
        return audio
        
    def remove_noise(self, audio: np.ndarray) -> np.ndarray:
        """Apply noise reduction using spectral gating"""
        try:
            if len(audio) == 0:
                return audio
                
            # Convert to mono if stereo
            if len(audio.shape) > 1 and audio.shape[1] > 1:
                audio = np.mean(audio, axis=1)
                
            # Apply short-time Fourier transform
            stft = librosa.stft(audio, n_fft=2048, hop_length=512)
            magnitude = np.abs(stft)
            
            # Estimate noise from first few frames (assuming silence at start)
            noise_estimate = np.mean(magnitude[:, :10], axis=1, keepdims=True)
            
            # Apply spectral gating
            gain = np.maximum(1 - noise_estimate / (magnitude + 1e-8), 0.1)
            cleaned_stft = stft * gain
            
            # Convert back to time domain
            cleaned_audio = librosa.istft(cleaned_stft, hop_length=512)
            
            return cleaned_audio
            
        except Exception as e:
            logger.error(f"Noise reduction error: {e}")
            return audio
        
    def apply_filters(self, audio: np.ndarray) -> np.ndarray:
        """Apply bandpass filter for voice frequencies"""
        try:
            if len(audio) == 0:
                return audio
                
            # Bandpass filter for human voice (80Hz - 8000Hz)
            low_freq = 80
            high_freq = 8000
            
            nyquist = self.sample_rate / 2
            low = low_freq / nyquist
            high = high_freq / nyquist
            
            # Design Butterworth filter
            b, a = signal.butter(4, [low, high], btype='band')
            
            # Apply filter
            filtered_audio = signal.filtfilt(b, a, audio)
            
            return filtered_audio
            
        except Exception as e:
            logger.error(f"Filter application error: {e}")
            return audio
        
    def detect_speech_activity(self, audio: np.ndarray, threshold=0.01) -> bool:
        """Detect if audio contains speech"""
        if audio is None or len(audio) == 0:
            return False
            
        energy = np.mean(audio ** 2)
        return energy > threshold
        
    def enhance_audio(self, audio: np.ndarray) -> np.ndarray:
        """Apply comprehensive audio enhancement"""
        try:
            if len(audio) == 0:
                return audio
                
            # Step 1: Normalize
            audio = self.normalize_audio(audio)
            
            # Step 2: Apply filters
            audio = self.apply_filters(audio)
            
            # Step 3: Remove noise
            audio = self.remove_noise(audio)
            
            # Step 4: Final normalization
            audio = self.normalize_audio(audio)
            
            return audio
            
        except Exception as e:
            logger.error(f"Audio enhancement error: {e}")
            return audio
            
    def get_audio_features(self, audio: np.ndarray) -> dict:
        """Extract audio features for analysis"""
        try:
            if len(audio) == 0:
                return {}
                
            features = {
                'energy': np.mean(audio ** 2),
                'rms': np.sqrt(np.mean(audio ** 2)),
                'zero_crossing_rate': np.sum(np.diff(np.sign(audio)) != 0) / len(audio),
                'spectral_centroid': np.mean(librosa.feature.spectral_centroid(y=audio, sr=self.sample_rate)),
                'spectral_rolloff': np.mean(librosa.feature.spectral_rolloff(y=audio, sr=self.sample_rate))
            }
            
            return features
            
        except Exception as e:
            logger.error(f"Feature extraction error: {e}")
            return {}
