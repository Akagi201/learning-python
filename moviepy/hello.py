#!/usr/bin/env python

from moviepy.editor import *

video = VideoFileClip("sample.mp4").subclip(50, 60)

# Make the text. Many more options are available.
txt_clip = (TextClip("aksample",fontsize=70,color='red').set_position('center').set_duration(10))

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("o.webm", fps=25)