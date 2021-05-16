from tkinter import *
from pytube import YouTube

#Creating Display Window
root = Tk()
root.geometry('550x350')
root.resizable(0,0)
root.title("Bhupendra-youtube video downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold', bg = 'green').pack()


#Creating Field to enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x = 160, y = 80)
link_enter = Entry(root, width = 80,textvariable = link).place(x = 32, y = 130)

#Creating function to start downlod
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 17').place(x= 180 , y = 240)  
Button(root,text = 'DOWNLOAD', font = 'arial 17 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=180 ,y = 180)
root.mainloop()





