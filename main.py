from pytube import YouTube

url = "https://www.youtube.com/watch?v=2zNSgSzhBfM"
 
yt = YouTube(url)
print(yt.views,yt.title)