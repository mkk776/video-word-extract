import whisper_timestamped as whisper
import subprocess as sp
from time import sleep
import torch
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

file = "test_file.mp4"
model_data = "medium"

audio = whisper.load_audio(file)

clear()
print("running on GPU" if torch.cuda.is_available() else "no cuda found, running on CPU")

model = whisper.load_model(model_data, device="cuda:0" if torch.cuda.is_available() else "cpu")

result = whisper.transcribe(model, audio, language="en")

print('')

lis = []
for segment in result['segments']:
    for word in segment['words']:
        word_text=word['text'].replace(',', '').replace('.', '').replace('?', '').lower()
        if word_text == 'it':#word_text.startswith('m') and word_text.endswith('orp'):#                                      change this as you like
            print(word_text, ' '*(16-len(word_text)), str(round(word['start'], 4)), '<-->', str(round(word['end'], 4)), '          SEGMENT')
            lis.append([word_text, str(round(word['start'], 4)), str(round(word['end'], 4))])
        else:
            print(word_text, ' '*(16-len(word_text)), str(round(word['start'], 4)), '<-->', str(round(word['end'], 4)))
            
print('')

if len(lis)==0:
    print('not segments found!')
    exit()

print(len(lis), 'segments found, combining...')

trim_start = -0.2
trim_end   = -0.2

mid=''
for i in lis:
    start = round(float(i[1])+trim_start, 4)
    diff = round(float(i[2])-trim_end-start, 4)

    if start<0:
        start=0
    if diff<0.01:
        diff=0.01
    
    print(i[0]+' '*(max([len(i[0]) for i in lis])+2-len(i[0])), start, '<-->', round(start+diff, 4))

    end = round(start+diff, 4)

    mid+='between(t,'+str(start)+','+str(end)+')+'
    
print('')

mid=mid[:-1]

command = 'ffmpeg -y -loglevel info -i '+file+' -vf "select=' + "'" + mid + "'" + ', setpts=N/FRAME_RATE/TB" -af "aselect=' + "'" + mid + "'" +', asetpts=N/SR/TB" out.mp4'
os.system(command)