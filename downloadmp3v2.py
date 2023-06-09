#---------------------------------------------------------
# Youtube to MP3 Downloader with UI
# Downloader referenced from https://youtu.be/t-ZsQ20Gdyo
# UI made by me using tkinter
#----------------------------------------------------------

#imports -----------------------------------------------------------------------------------------------------------------------------------------------------------------
from pytube import YouTube
import os
from tkinter import *

#functions ---------------------------------------------------------------------------------------------------------------------------------------------------------------
def download():
    yt = YouTube(input('Enter the Url of the video you want to download: '))
    video = yt.streams.filter(only_audio=True).first()
    destination = "/Users/flami/Music/spotify"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + ' has been successfully downloaded')

#main window -------------------------------------------------------------------------------------------------------------------------------------------------------------
main_window = Tk(className = "mp3downloader")
main_window.geometry("1180x900")

#background --------------------------------------------------------------------------------------------------------------------------------------------------------------
cRect1 = Canvas(width=1180, height=800)
cRect1.create_rectangle(1180,800,0,0, outline='#121212', fill="#121212")
cRect1.place(x=0, y=0)

#shapes ------------------------------------------------------------------------------------------------------------------------------------------------------------------
cRect2 = Canvas(width=400, height=700)
cRect2.create_rectangle(1080,700,0,0, outline='#212121', fill="#212121", width=20 )
cRect2.place(x=50, y=30)

cRect3 = Canvas(width=650, height=700)
cRect3.create_rectangle(1080,700,0,0, outline='#212121', fill="#212121", width=20 )
cRect3.place(x=480, y=30)

#buttons -----------------------------------------------------------------------------------------------------------------------------------------------------------------
b1 = Button(text="GO!", bg="#1db954", fg = "white", font=("System", 20), command=download())
b1.place(x=750, y= 600)


#labels ------------------------------------------------------------------------------------------------------------------------------------------------------------------
title = Label(main_window, text = "YouTube to MP3 Downloader", fg = 'white', bg= "#212121", font=("System", 20))
title.place(x=60, y=50)

#labels for video URL
video_label = Label(main_window, text= "Enter YouTube URL here: ", fg = 'white', bg= "#212121", font=("System", 16, 'underline'))
video_label.place(x=500, y=110)
video_example_label = Label(main_window, text= "Example:  https://www.youtube.com/watch?v=dQw4w9WgXcQ ", fg = '#b3b3b3', bg= "#212121", font=("System", 10))
video_example_label.place(x=510, y=140)

#input label for video URL
url_input = Entry(main_window, width=16, fg = 'white', bg= "#121212", font=("System", 14,) )
url_input.place(x=510, y=170)

#labels for path
path_label = Label(main_window, text= "Enter Folder path here: ", fg = 'white', bg= "#212121", font=("System", 16))
path_example_label = Label(main_window, text= "Example:  /Users/user1/Music  ", fg = '#b3b3b3', bg= "#212121", font=("System", 10))
path_label.place(x=500, y=210)
path_example_label.place(x=510, y=230)

#input label for path
path_input = Entry(main_window, width=16, fg = 'white', bg= "#121212", font=("System", 14,) )
path_input.place(x=510, y=260)

instructions = Label(main_window, text = "Instructions:", fg = 'white', bg = "#212121", font=("System", 14, "bold", 'underline'))
instructions.place(x=60, y=110)

i_text1 = Label(main_window, text = "Copy the URL of the YouTube video you want to ", fg = 'white', bg = "#212121", font=("System", 14))
i_text2 = Label(main_window, text= " download. Then enter the path of the folder you ", fg = 'white', bg = "#212121", font=("System", 14))
i_text3 = Label(main_window, text=" want your mp3 to be downloaded to.", fg = 'white', bg = "#212121", font=("System", 14))

i_text1.place(x=60, y=140)
i_text2.place(x=60, y=160)
i_text3.place(x=60, y=180)

main_window.mainloop()

