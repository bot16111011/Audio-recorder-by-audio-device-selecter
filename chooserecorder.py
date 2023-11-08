import pyaudio
import wave

# Detect devices and get a list of available audio devices
p = pyaudio.PyAudio()
host_info = p.get_host_api_info_by_index(0)
device_count = host_info.get('deviceCount')
devices = []
# Iterate between devices:
for i in range(0, device_count):
    device = p.get_device_info_by_host_api_device_index(0, i)
    devices.append(device['name'])

# Print the list of available devices
print("Available audio devices:")
for i, device in enumerate(devices):
    print(f"{i + 1}. {device}")

# Ask the user to select a device for recording
selected_device_index = int(input("Enter the number of the device you want to use: ")) - 1
selected_device_info = p.get_device_info_by_index(selected_device_index)

print("Selected device properties:")
print(selected_device_info)

# Adjust the number of channels based on the selected device's capabilities
CHANNELS = selected_device_info['maxInputChannels'] 

# Check if the selected index is valid
if 0 <= selected_device_index < len(devices) and CHANNELS>0:
    selected_device_name = devices[selected_device_index]
    print(f"Recording audio from {selected_device_name}...")
    
    # Set up the audio stream using the selected device
    CHUNK = 1024  # Number of frames per buffer
    FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
    # CHANNELS = 2  # Number of audio channels (stereo)
    RATE = 44100  # Sample rate (samples per second)
    frames=[]
    audio_stream = p.open(format=FORMAT,
                          channels=CHANNELS,
                          rate=RATE,
                          input=True,
                          input_device_index=selected_device_index,
                          frames_per_buffer=CHUNK)
    
    try:
        # Start recording audio
        while True:
            data = audio_stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Recording stopped.")
        audio_stream.stop_stream()
        audio_stream.close()
        p.terminate()
        with wave.open('output.wav', 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
else:
    print("Invalid device number or output device is selected. Exiting...")
