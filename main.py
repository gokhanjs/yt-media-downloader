from pytube import YouTube
import time

def getVideoInfo():
    print('Its Working!')

def downloadVideo():
    print('Its Working 2!')


'''#url = input("Enter Video Url: ")
url = "https://www.youtube.com/watch?v=2zNSgSzhBfM"
yt = YouTube(url)
print(yt.title+" adlı video indiriliyor...")
print('*********')
yt.streams.get_highest_resolution().download()
#print(yt.streams.filter(progressive=True))'''

val = input('Video indirmek için "1", Müzik indirmek için "2":')
choice = ''
if val == "1":
    print('Video indirmek için yönlendiriliyorsunuz.')
    choice = 'V'
elif val == "2":
    print('Müzik indirmek için yönlendiriliyorsunuz.')
    choice = 'M'
else:
    print('Geçersiz İşlem!')


url = input('İndirmek istediğiniz video linkini yazınız:')
try:
    yt = YouTube(url)
except:
  print("Hata!")

if choice == 'V':
    print('İndiriliyor Lütfen Bekleyin!')
    yt.streams.get_highest_resolution().download()
elif choice == 'M':
    print('İndiriliyor Lütfen Bekleyin!')
    yt.streams.get_by_itag(140).download()
else:
    print('Bişey Oldu!')

print('İşlem Tamam!')



