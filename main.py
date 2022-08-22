
from pytube import YouTube

url = ''
my_video = YouTube(url)

for stream in my_video.streams:
    print(stream)

my_video = my_video.streams.filter(res="1080p", mime_type="video/webm").first()

my_video.download()

my_video = YouTube(url)

for stream in my_video.streams:
    print(stream)

my_video = my_video.streams.filter(abr="128kbps", mime_type="audio/mp4").first()
my_video.download()
