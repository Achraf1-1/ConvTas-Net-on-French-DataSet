import os
from pydub import AudioSegment
import wave
import contextlib

def get_duration_wav(file_path):
    with contextlib.closing(wave.open(file_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration

audio_files = []
files=[]
directory = "./WAV/"
for filename in os.listdir(directory):
    files.append(filename)

input_path = "./WAV/"
output_path = "./Output/"
if __name__ == "__main__":
    for i in range(len(files)):
        file1 = files[i] # get the first file in the folder
        path1 = input_path + file1 # path of the first path
        print(path1+'/')
        for filename in os.listdir(path1):
            audio_files.append(filename)
            sound1 = AudioSegment.from_wav(path1+'/'+filename) # the first file
            for j in range(i+1, len(files)):
                file2 = files[j]
                path2 = input_path + file2
                for filename2 in os.listdir(path2+'/'):
                    audio_files.append(filename)
                    sound2 = AudioSegment.from_wav(path2+'/'+filename2) # the second file
                    path3 = output_path + file1[:-4] + "+" + file2[:-4] + ".wav" # name of the new file(file1+file2)
                    if get_duration_wav(path1) <= get_duration_wav(path2):
                        output = sound1.overlay(sound2) # overlay audio
                    else:
                        output = sound2.overlay(sound1)
                        output.export(path3, format="wav") # save the file
