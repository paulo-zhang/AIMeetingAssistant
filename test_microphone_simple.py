"""
Simple microphone test script
This script tests basic microphone functionality without requiring all dependencies
"""

def test_microphone_simple():
    """Simple microphone test using only built-in libraries"""
    print("🎤 Simple Microphone Test")
    print("=" * 40)
    
    try:
        # Try to import sounddevice
        import sounddevice as sd
        import numpy as np
        
        print("✅ Dependencies loaded successfully")
        
        # List available audio devices
        print("\n📱 Available audio devices:")
        devices = sd.query_devices()
        for i, device in enumerate(devices):
            if device['max_input_channels'] > 0:
                print(f"  {i}: {device['name']} (Input channels: {device['max_input_channels']})")
        
        # Test recording
        print("\n🎙️ Testing microphone...")
        print("Speak into your microphone for 3 seconds...")
        
        duration = 3
        sample_rate = 16000
        
        # Record audio
        audio_data = sd.rec(int(duration * sample_rate), 
                           samplerate=sample_rate, 
                           channels=1, 
                           dtype=np.float32)
        sd.wait()  # Wait until recording is finished
        
        # Analyze the recorded audio
        max_amplitude = np.max(np.abs(audio_data))
        rms_amplitude = np.sqrt(np.mean(audio_data ** 2))
        
        print(f"\n📊 Audio Analysis:")
        print(f"  Maximum amplitude: {max_amplitude:.4f}")
        print(f"  RMS amplitude: {rms_amplitude:.4f}")
        
        # Determine if microphone is working
        if max_amplitude > 0.01:
            print("✅ Microphone is working! Audio detected.")
            return True
        else:
            print("❌ No audio detected. Check microphone settings.")
            return False
            
    except ImportError as e:
        print(f"❌ Missing dependencies: {e}")
        print("\nTo install required packages:")
        print("  python -m pip install sounddevice numpy")
        return False
        
    except Exception as e:
        print(f"❌ Error during microphone test: {e}")
        return False

def test_microphone_permissions():
    """Test microphone permissions without recording"""
    print("\n🔐 Testing microphone permissions...")
    
    try:
        import sounddevice as sd
        
        # Try to query devices (this tests permissions)
        devices = sd.query_devices()
        input_devices = [d for d in devices if d['max_input_channels'] > 0]
        
        if input_devices:
            print(f"✅ Found {len(input_devices)} input device(s)")
            print("✅ Microphone permissions are working")
            return True
        else:
            print("❌ No input devices found")
            return False
            
    except Exception as e:
        print(f"❌ Permission test failed: {e}")
        return False

def main():
    """Main test function"""
    print("AI Meeting Assistant - Microphone Test")
    print("=" * 50)
    
    # Test 1: Permissions
    permissions_ok = test_microphone_permissions()
    
    if not permissions_ok:
        print("\n💡 Troubleshooting tips:")
        print("1. Check Windows microphone privacy settings")
        print("2. Ensure microphone is set as default input device")
        print("3. Try running PowerShell as administrator")
        print("4. Check if microphone is working in other applications")
        return
    
    # Test 2: Actual recording
    print("\n" + "=" * 50)
    recording_ok = test_microphone_simple()
    
    if recording_ok:
        print("\n🎉 Microphone test completed successfully!")
        print("You can now proceed with the full audio capture test.")
        print("\nNext steps:")
        print("1. Install all dependencies: python -m pip install -r requirements.txt")
        print("2. Run full test: python test_audio.py")
    else:
        print("\n💡 Troubleshooting tips:")
        print("1. Check microphone volume levels")
        print("2. Ensure microphone is not muted")
        print("3. Test microphone in Windows Sound settings")
        print("4. Try a different microphone")

if __name__ == "__main__":
    main()
