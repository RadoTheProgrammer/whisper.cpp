# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import datetime
now = datetime.datetime.now()
# Sampling frequency
freq = 44100

# Recording duration
duration = 60

# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
print(recording)
print("Recording...")
# Record audio for the given number of seconds
sd.wait()
print(recording.shape)
print("Recording complete")
# This will convert the NumPy array to an audio
# file with the given sampling frequency


# Convert the NumPy array to audio file
wv.write(rf"myproject\recording-{now.strftime("%Y-%m-%d_%H-%M-%S")}.wav", recording, freq, sampwidth=2)
