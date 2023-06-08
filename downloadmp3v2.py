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
main_window = Tk(className = "mp3downloader")
main_window.geometry("1180x900")

#background -------------------------------------------------
cRect1 = Canvas(width=1180, height=800)
cRect1.create_rectangle(1180,800,0,0, outline='#272727', fill="#272727", width='1')
cRect1.place(x=0, y=0)

cRect2 = Canvas(width=1080, height=700)
cRect2.create_rectangle(1080,700,0,0, outline='#535353', fill="#535353", width = '1')
cRect2.place(x=50, y=50)

#shapes -----------------------------------------------------

#buttons ----------------------------------------------------

#inputs ------------------------------------------------------

#labels -----------------------------------------------------
title = Label(main_window, text = "YouTube to MP3 Downloader", fg = 'white', bg= "#535353", font=("Gotham", 20))
title.place(x=50, y=50)

main_window.mainloop()

def download():
    yt = YouTube(input('Enter the Url of the video you want to download: '))
    video = yt.streams.filter(only_audio=True).first()
    destination = "/Users/flami/Music/spotify"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + ' has been successfully downloaded')