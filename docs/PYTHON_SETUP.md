# Python Installation and Audio Capture Testing Guide

## Prerequisites Check

Before testing the audio capture functionality, you need to ensure Python is properly installed on your Windows system.

## Step 1: Install Python

### Option A: Install from Microsoft Store (Recommended)
1. Open Microsoft Store
2. Search for "Python 3.11" or "Python 3.12"
3. Click "Install" on the official Python package
4. This will automatically add Python to your PATH

### Option B: Install from Python.org
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or 3.12 for Windows
3. **IMPORTANT**: During installation, check "Add Python to PATH"
4. Run the installer as administrator

### Option C: Install via Chocolatey (if you have it)
```powershell
choco install python
```

## Step 2: Verify Python Installation

After installation, open a new PowerShell window and run:
```powershell
python --version
# Should output: Python 3.x.x

python -m pip --version
# Should output: pip version information
```

## Step 3: Set Up Virtual Environment

```powershell
# Navigate to your project directory
cd C:\Code\AIMeetingAssistant

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Verify activation (should show (venv) in prompt)
```

## Step 4: Install Dependencies

```powershell
# Make sure virtual environment is activated
# Install core dependencies
python -m pip install --upgrade pip
python -m pip install numpy
python -m pip install sounddevice
python -m pip install loguru

# Install additional dependencies
python -m pip install -r requirements.txt
```

## Step 5: Test Audio Capture

### Basic Test
```powershell
python test_audio.py
```

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

### Issue 1: PyAudio Installation Error
**Error**: `Microsoft Visual C++ 14.0 is required`

**Solutions**:
1. Install Visual Studio Build Tools:
   - Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Install "C++ build tools" workload

2. Use pre-compiled wheels:
   ```powershell
   python -m pip install pipwin
   pipwin install pyaudio
   ```

3. Use conda instead:
   ```powershell
   conda install pyaudio
   ```

### Issue 2: Microphone Not Detected
**Error**: `No default input device available`

**Solutions**:
1. Check Windows Sound Settings:
   - Right-click speaker icon → "Open Sound settings"
   - Go to "Input" → Select your microphone
   - Test microphone

2. Check Privacy Settings:
   - Windows Settings → Privacy → Microphone
   - Allow apps to access microphone
   - Allow desktop apps to access microphone

3. Run as Administrator:
   ```powershell
   # Right-click PowerShell → "Run as administrator"
   cd C:\Code\AIMeetingAssistant
   venv\Scripts\activate
   python test_audio.py
   ```

### Issue 3: Audio Quality Issues
**Symptoms**: Poor audio quality, noise, or distortion

**Solutions**:
1. Check microphone levels in Windows Sound settings
2. Ensure good microphone positioning
3. Test with different microphones
4. Adjust audio enhancement settings in Windows

## Alternative Testing Method

If the main test fails, try this simplified test:

```python
# Create test_simple.py
import sounddevice as sd
import numpy as np
import time

def test_microphone():
    print("Testing microphone...")
    print("Speak into your microphone for 3 seconds...")
    
    # Record audio for 3 seconds
    duration = 3
    sample_rate = 16000
    
    audio_data = sd.rec(int(duration * sample_rate), 
                       samplerate=sample_rate, 
                       channels=1, 
                       dtype=np.float32)
    sd.wait()  # Wait until recording is finished
    
    # Check if we got audio
    max_amplitude = np.max(np.abs(audio_data))
    print(f"Maximum audio amplitude: {max_amplitude}")
    
    if max_amplitude > 0.01:
        print("✅ Microphone is working!")
    else:
        print("❌ No audio detected. Check microphone settings.")

if __name__ == "__main__":
    test_microphone()
```

Run with:
```powershell
python test_simple.py
```

## Next Steps

Once audio capture is working:

1. **Push code to GitHub**:
   ```powershell
   git add .
   git commit -m "Add Python installation guide and audio testing"
   git push origin master
   ```

2. **Continue with speech recognition**:
   - Install Whisper: `python -m pip install openai-whisper`
   - Test speech-to-text functionality

3. **Add language model integration**:
   - Get OpenAI API key
   - Test GPT-4 integration

## Quick Commands Summary

```powershell
# Install Python (via Microsoft Store or python.org)
# Open new PowerShell window
cd C:\Code\AIMeetingAssistant
python -m venv venv
venv\Scripts\activate
python -m pip install numpy sounddevice loguru
python test_audio.py
```
