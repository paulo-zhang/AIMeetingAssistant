# Quick Start Guide

## Prerequisites

- Python 3.9 or higher
- Microphone access
- Internet connection for API services

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-meeting-assistant.git
cd ai-meeting-assistant
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example environment file
cp env.example .env

# Edit .env with your API keys
# You'll need at least one of these:
# - OpenAI API key (for GPT-4 and Whisper)
# - Azure Speech Services key (for TTS)
# - Anthropic API key (for Claude)
```

## Testing Audio Capture

### Basic Audio Test
```bash
python test_audio.py
```

This will:
- Start audio capture from your microphone
- Process the audio in real-time
- Detect speech activity
- Display audio features

### Expected Output
```
2024-01-01 12:00:00 | INFO | Starting audio capture test...
2024-01-01 12:00:00 | INFO | Starting audio capture...
2024-01-01 12:00:00 | INFO | Recording for 10 seconds... (speak into your microphone)
2024-01-01 12:00:01 | INFO | Speech detected!
2024-01-01 12:00:01 | INFO | Audio features: {'energy': 0.123, 'rms': 0.351, ...}
2024-01-01 12:00:10 | INFO | Stopping audio capture...
2024-01-01 12:00:10 | INFO | Test completed successfully!
```

## Troubleshooting

### Common Issues

#### 1. PyAudio Installation Error
**Error**: `Microsoft Visual C++ 14.0 is required`

**Solution**: Install Visual Studio Build Tools or use conda:
```bash
conda install pyaudio
```

#### 2. Microphone Not Detected
**Error**: `No default input device available`

**Solution**: 
- Check microphone permissions in your OS
- Ensure microphone is set as default input device
- Try running as administrator (Windows)

#### 3. Audio Quality Issues
**Symptoms**: Poor audio quality, noise, or distortion

**Solutions**:
- Check microphone settings in OS
- Ensure good microphone positioning
- Adjust audio levels in system settings

### Getting Help

1. Check the [Implementation Plan](IMPLEMENTATION_PLAN.md) for detailed technical information
2. Review the [README](README.md) for project overview
3. Open an issue on GitHub for bugs or feature requests

## Next Steps

After successful audio capture testing:

1. **Add Speech Recognition**: Integrate Whisper for real-time transcription
2. **Language Model Integration**: Add GPT-4 for intelligent responses
3. **Voice Synthesis**: Implement text-to-speech capabilities
4. **Visual Content**: Add image generation and drawing features

## Development Workflow

1. **Test each component** individually before integration
2. **Use the test scripts** to verify functionality
3. **Check logs** for debugging information
4. **Incremental development** - add features one by one

## API Keys Required

For full functionality, you'll need:

- **OpenAI API Key**: For GPT-4 (language model) and Whisper (speech recognition)
- **Azure Speech Services**: For high-quality text-to-speech
- **ElevenLabs**: For voice cloning (optional)
- **Meeting Platform APIs**: For Zoom/Teams integration (optional)

Start with OpenAI API key for basic functionality.
