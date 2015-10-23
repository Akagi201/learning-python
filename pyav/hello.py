
import av

container = av.open('video.mp4')
video = next(s for s in container.streams if s.type == b'video')

for packet in container.demux(video):
    for frame in packet.decode():
        frame.to_image().save('frame-%04d.jpg' % frame.index)
