#!/usr/bin/env python

import subprocess as sp
import numpy

cmd = ["ffmpeg",
       "-i", "BlackBerry.mp4",
       "-f", "image2pipe",
       "-pix_fmt", "rgb24",
       "-vcodec", "rawvideo",
       "-"]

pipe = sp.Popen(cmd, stdout=sp.PIPE, bufsize=10 ** 8)

# # read 380*480*3 bytes (= 1 frame)
# raw_image = pipe.stdout.read(320*180*3)
# # transform the byte read into a numpy array
# image =  numpy.fromstring(raw_image, dtype='uint8')
# image = image.reshape((180,320,3))
# # throw away the data in the pipe's buffer.
# pipe.stdout.flush()

# seek https://trac.ffmpeg.org/wiki/Seeking
# command = ["ffmpeg",
#            '-ss', '00:59;59',
#            '-i', 'myHolidays.mp4',
#            '-ss', '1',
#            '-f', 'image2pipe',
#            '-pix_fmt', 'rgb24',
#            '-vcodec', 'rawvideo', '-']
# pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=10 ** 8)
