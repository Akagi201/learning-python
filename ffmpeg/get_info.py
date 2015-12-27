
import subprocess as sp

cmd = ['ffmpeg', '-i', 'BlackBerry.mp4', '-']
pipe = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
pipe.stdout.readline()
pipe.terminate()
infos = pipe.stderr.read()
print(infos)
