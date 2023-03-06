import librosa
import os
filename = '.wav'
newFilename = 'C.wav'

y, sr = librosa.load(filename, sr=16000)
y_8k = librosa.resample(y,sr,8000)

librosa.output.write_wav(newFilename, y_8k, 8000)
