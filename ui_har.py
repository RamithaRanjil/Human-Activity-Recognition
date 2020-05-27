from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.messagebox
import os
from har import *

def open_webcam():
    openWebCamera()

def open_videofile():
    pass
    
window = Tk()
#window.geometry("550x300+300+150")
window.geometry("600x400")
window.resizable(width=True, height=True)
window.configure(bg='light coral')
l = Label(window,text='Human Activity Recognition',font=("Arial Bold",30),bg="Deep pink4").pack()

btn1 = Button(window, text='Open Web Cam', command=open_webcam,bg="pale violet red",fg="maroon").pack()
window.mainloop()
