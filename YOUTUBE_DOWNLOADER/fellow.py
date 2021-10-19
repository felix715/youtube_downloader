# you need to install tkinter and pytube from their gihub account
# then just import the following:
from pytube import YouTube
from tkinter import *
from pytube import Playlist
from tkinter import messagebox
   root=Tk()
# then here lets put our youtube image icon that is..... and not necessary needed...but is for the purpose of making our straff clean

# i decided to call it winicon
winicon=PhotoImage(file="........")
root.Iconphoto(False,winicon)
# background of the application and for tkinter is to as command configure and have set it to black
root.configure(bg="BLACK")
root.configure(bg="#205478")
root.Title("YouTube Downloader")
# setting the y and x axis
root.geometry("450*400")
root.resizable(width=0,height=0)


label = Label(root,text= "YouTube Downloader",bg="red",fg="white",font="bold",width=10,borderwidth=10,padx=10,pady=13)
label.grid(row=0,columnspan=3,padx=10,pady=10)
label.place(x=20,y=10)


label=Label(root,text="Download Video",font="bold",bg="black",fg="white",width=30)
label.place(x=90,y=85)

tube_entry1 = stringVar()
entry1=Entry(root,width=45,bd=6,borderwidth6,font=14,textvariable=tube_entry1)
entry1.insert(0,"Youtube video link")
entry1.grid(row=1,column=1,columnspan=10,padx=10,pady=13)
entry1.place(x=10,y=120)



# single download function
def download_single():
    url =entry1.get()
    try:
        YouTube(url).streams.first().download()
        yt=YouTube(url)
        yt.streams.filter(progressive=True,file_extensions="mp4").order_by("resolution").desc().first().download() messagebox.showInfo("Success","Video Downloader")
    except:
        # if there is an error the tkinter will display the message on whta is going on the application
        messagebox.showerror("error","please insert the url")
button_single =Button(root,text="Download",bg="red",fg="white",command=download_single,pady=20,padx=10)

button_single.place(x=150,y=165)








   root.mainloop()