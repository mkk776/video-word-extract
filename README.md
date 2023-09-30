# video-word-extract
Have a video and you want to just get the scenes with what word? I think you are in the right place...

How it works?
  1) It finds the words including their start end finish using whisper_timesampled created from whisper(openai).
  2) It selects spesific words.
  3) Combines using ffmpeg.

simple, isn't it?

if you are using windows install git
https://git-scm.com/download/win

install cuda 11.8
https://developer.nvidia.com/cuda-11-8-0-download-archive

here's a example
https://youtu.be/2s5zXx3XN8U
