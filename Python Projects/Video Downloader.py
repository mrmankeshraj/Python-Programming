from pytube import YouTube

link = "https://www.youtube.com/watch?v=FIpbrnbVfJk"
you_tube = YouTube(link)

print(you_tube.title)
print(you_tube.thumbnail_url)

videos = you_tube.streams.filter(only_video=True)
vid = list(enumerate(videos))

for i in vid:
	print(i)
stream = int(input("Enter your Choice : "))
videos[stream].download()
print("Download Successfull")


# ***** FOR PLAYLIST DOWNLOAD *****
from pytube import Playlist

py = Playlist("https://www.youtube.com/watch?v=0VdzZQdaZ28&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv")
print(f'Downloading : {py.title}')

for video in py.videos:
	video.streams.first().download()