# Audio Recorder

This Python script allows you to record audio from a specific input device on your system. It uses the PyAudio library to detect and interact with audio devices connected to your computer. You can select an input device from the available options and record audio until you manually stop the process. The recorded audio is saved as a WAV file named `output.wav` in the same directory as the script.

## Prerequisites

Before running the script, make sure you have Python installed on your system. You can install the required dependencies using the following command:

```bash
pip install pyaudio
pip install wave
```

## Usage

1. Run the script using Python:

   ```bash
   python chooserecorder.py
   ```

2. The script will display a list of available audio devices. Choose the device you want to use by entering the corresponding number.

3. Once you've selected a device, the script will start recording audio from that device.

4. To stop the recording, press `Ctrl + C`. The recorded audio will be saved as `output.wav` in the same directory as the script.

## Notes

- Make sure to connect a valid input device to your system before running the script.
- Adjust the `CHUNK` size and `FORMAT` variable in the script according to your preferences.
- The recorded audio will be saved in 16-bit PCM format with a sample rate of 44100 Hz.

Feel free to customize and integrate this script into your projects as needed! If you encounter any issues or have suggestions for improvements, please open an issue or create a pull request. Happy recording!
