#pip install pytube
from pytube import YouTube
yt = Youtube('https://www.youtube.com/watch?v=A-rEb0KuopI')
yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution')[-1].download()