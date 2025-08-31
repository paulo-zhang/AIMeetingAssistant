"""
Audio Processing Module

Handles real-time audio capture, processing, and streaming capabilities
for the AI meeting assistant.
"""

from .capture import AudioCapture
from .processing import AudioProcessor

__all__ = ['AudioCapture', 'AudioProcessor']
