from pytube import YouTube
import time


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



