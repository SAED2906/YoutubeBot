
from pytube import YouTube
import sys

url = sys.argv[1]
my_video = YouTube(url)

#for stream in my_video.streams:
    #print(stream)
try:
    my_video = YouTube(url)
    my_video = my_video.streams.filter(res="1080p", mime_type="video/mp4").first()
    my_video.download()
    #print("Found 1080p")
except:
    #print("Error no 1080p")
    try:
        my_video = YouTube(url)
        my_video = my_video.streams.filter(res="720p", mime_type="video/mp4").first()
        my_video.download()
       # print("Found 720p")
    except:
        #print("Error no 720p")
        try:
            my_video = YouTube(url)
            my_video = my_video.streams.filter(res="480p", mime_type="video/mp4").first()
            my_video.download()
           # print("Found 480p")
        except:
            #print("Error no 480p")
            try:
                my_video = YouTube(url)
                my_video = my_video.streams.filter(res="360p", mime_type="video/mp4").first()
                my_video.download()
               # print("Found 360p")
            except:
               # print("Error no 360p")


my_video = YouTube(url)
#for stream in my_video.streams:
    #print(stream)


try:
    my_video = YouTube(url)
    my_video = my_video.streams.filter(abr="160kbps", mime_type="audio/webm").first()
    my_video.download()
    #print("Found 160kbps")
except:
    #print("Error no 160kbps")
    try:
        my_video = YouTube(url)
        my_video = my_video.streams.filter(abr="128kbps", mime_type="audio/webm").first()
        my_video.download()
        #print("Found 128kbps")
    except:
        #print("Error no 128kbps")
        try:
            my_video = YouTube(url)
            my_video = my_video.streams.filter(abr="70kbps", mime_type="audio/webm").first()
            my_video.download()
            #print("Found 70kbps")
        except:
            #print("Error no 70kbps")
            try:
                my_video = YouTube(url)
                my_video = my_video.streams.filter(abr="50kbps", mime_type="audio/webm").first()
                my_video.download()
                #print("Found 50kbps")
            except:
                #print("Error no 50kbps")

#my_video = my_video.streams.filter(abr="128kbps", mime_type="audio/mp4").first()
#my_video.download()
print(sys.argv[1])
