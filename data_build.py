
###This code is used to build the dataset
import os
from pydub import AudioSegment
import librosa
import wave
import contextlib

def get_duration_wav(file_path):
    with contextlib.closing(wave.open(file_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    return duration
 
output_path = r""  # output path 
input_path1 = r""  # source path
for file1 in os.listdir(input_path1):  # get the first file in the folder
    
    path1 = input_path1 + "\\" + file1  # path of the first path  
    sound1 = AudioSegment.from_wav(path1)  # the first file
    for file2 in os.listdir(input_path1):
        if file1[0:2]!=file2[0:2]:
            path2= input_path1 + "\\" + file2
            sound2 = AudioSegment.from_wav(path2)  # the second file
            path3 = output_path + "\\" + file1+"+"+file2  # name of the new file(file1+file2)
            if get_duration_wav(path1)<=get_duration_wav(path2):
                output = sound1.overlay(sound2)  # overlay audio
                output.export(path3, format="wav")  # save the file

