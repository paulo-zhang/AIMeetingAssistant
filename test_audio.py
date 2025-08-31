"""
Test script for audio capture functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import time
from src.audio.capture import AudioCapture
from src.audio.processing import AudioProcessor
from loguru import logger

def audio_callback(audio_data):
    """Callback function for audio data"""
    # Process the audio data
    processor = AudioProcessor()
    enhanced_audio = processor.enhance_audio(audio_data)
    
    # Check if there's speech activity
    is_speaking = processor.detect_speech_activity(enhanced_audio)
    
    if is_speaking:
        logger.info("Speech detected!")
        # Extract features
        features = processor.get_audio_features(enhanced_audio)
        logger.info(f"Audio features: {features}")

def main():
    """Main test function"""
    logger.info("Starting audio capture test...")
    
    # Initialize audio capture
    capture = AudioCapture(sample_rate=16000, chunk_size=1024)
    
    try:
        # Start capturing audio
        logger.info("Starting audio capture...")
        capture.start_capture(callback=audio_callback)
        
        # Run for 10 seconds
        logger.info("Recording for 10 seconds... (speak into your microphone)")
        time.sleep(10)
        
        # Stop capturing
        logger.info("Stopping audio capture...")
        capture.stop_capture()
        
        logger.info("Test completed successfully!")
        
    except KeyboardInterrupt:
        logger.info("Test interrupted by user")
        capture.stop_capture()
    except Exception as e:
        logger.error(f"Test failed: {e}")
        capture.stop_capture()

if __name__ == "__main__":
    main()
