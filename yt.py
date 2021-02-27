# video_list = ["https://www.youtube.com/watch?v=UT58ETAj3cg","https://www.youtube.com/watch?v=TH3d5cyeer0"]
# yt = YouTube("https://www.youtube.com/watch?v=UT58ETAj3cg")
# dw = yt.streams.first(22)
# dw.download("Videos")

#for downloading multipl videos using file handling
from pytube import YouTube
video_list = open("sample.txt","r")
for i in video_list:
    yt = YouTube(i)
    try:
        dw = yt.streams.first()#get_by_itag(22)
        dw.download("Videos/")
        print("downloaded",i)
    except:
        print("download failed for",i)

# importing single video in just two lines
#import pytube
#pytube.YouTube("https://www.youtube.com/watch?v=UT58ETAj3cg").streams.first().download("Videos/")

# for downloading whole playlist
# pytube.Playlist("https://www.youtube.com/watch?v=UT58ETAj3cg").download_all("Videos/")
