import sounddevice as sd
import soundfile as sf

def record_voice(file_path, duration=5, samplerate=44100, channels=2):
    try:
        print("Recording voice...")
        # Record audio
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels)
        sd.wait()  # Wait for the recording to complete

        # Save the recorded audio to a WAV file
        sf.write(file_path, audio_data, samplerate)

        print(f"Voice recorded and saved to {file_path}")
    except Exception as e:
        print("Error during recording:", str(e))

# Example usage
output_file_path = "recorded_voice.wav"  # Specify the file path to save the recorded audio
record_duration = 10  # Specify the duration of the recording in seconds

record_voice(output_file_path, duration=record_duration)
