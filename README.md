# video-word-extract
Have a video and you want to just get the scenes with what word? I think you are in the right place...

How it works?
  1) It finds the words including their start end finish using whisper_timesampled created from whisper(openai).
  2) It selects spesific words.
  3) Combines using ffmpeg.

simple, isn't it?
