from pytube import YouTube
from flask import Flask,render_template
import time


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/music")
def music():
    return render_template('music.html')

@app.route("/video")
def video():
    return render_template('video.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404


if __name__ == "__main__":
    app.run()


'''
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

print('İşlem Tamam!')'''





