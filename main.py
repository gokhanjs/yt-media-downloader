from flask import Flask,render_template,request,redirect,send_file
from pytube import YouTube
import time


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download",methods=['POST'])
def download():
    if request.method == 'POST':
        selection = request.form
        yt = YouTube(selection['url'])
        if selection['type'] == 'music':
            download_path = yt.streams.get_by_itag(140).download()
            fname = download_path.split('//')[-1]
            return send_file(fname, as_attachment=True)
            #return render_template('download.html',url = yt.streams.get_by_itag(140).url)
        elif selection['type'] == 'video':
            download_path = yt.streams.get_highest_resolution().download()
            fname = download_path.split('//')[-1]
            return send_file(fname, as_attachment=True)
            #return render_template('download.html',url = yt.streams.get_highest_resolution().url)
        else:
            return render_template('404.html'),404
        
        '''try:
            yt = YouTube(selection['url'])
            if selection['type'] == 'music':
                yt.streams.get_by_itag(140).download()
                path = '/'.yt.title.replace('.','') + '.mp4'
                send_file(path, as_attachment=True)
                return render_template('download.html',url = yt.streams.get_by_itag(140).url)
            elif selection['type'] == 'video':
                yt.streams.get_highest_resolution().download()
                path = yt.title.replace('.','') + '.mp4'
                send_file(path, as_attachment=True)
                return render_template('download.html',url = yt.streams.get_highest_resolution().url)
            else:
                return render_template('404.html'),404
        except:
            return render_template('404.html'),404'''
    else:
        return render_template('404.html'),404


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404

if __name__ == "__main__":
    app.run()






