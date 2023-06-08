#---------------------------------------------------------
# Youtube to MP3 Downloader with UI
# Downloader referenced from https://youtu.be/t-ZsQ20Gdyo
# UI made by me using tkinter
#----------------------------------------------------------

#imports -------------------------------------------------
from pytube import YouTube
import os
from tkinter import *


#main window -----------------------------------------------


yt = YouTube(input('Enter the Url of the video you want to download: '))
video = yt.streams.filter(only_audio=True).first()


destination = "/Users/flami/Music/spotify"
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print(yt.title + ' has been successfully downloaded')