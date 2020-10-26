import tkinter as tk
from tkinter import messagebox
import pygame
from pygame import mixer
from PIL import ImageTk
from tkinter import *
import PIL.Image

mixer.init()
root= tk.Tk()
mixer.music.load("welcome.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

canvas1 = tk.Canvas(root, width = 720, height = 640)
image = ImageTk.PhotoImage(PIL.Image.open("welcome.png"))
canvas1.create_image(0,0,anchor=NW, image=image)
canvas1.pack()
mixer.init()
def Photo():
    mixer.music.load("pic.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
    MsgBox = tk.messagebox.askquestion("Photo", "Hey you, Do you wanna take a photo ?")
    if MsgBox == 'yes':
        import process
        tk.messagebox.askquestion('Feedback', 'Do you wanna give us a Video Feedback ?')
        import video
        tk.messagebox.showinfo('Return', 'Thank you for your response...!')
    elif MsgBox == 'no':
        tk.messagebox.askquestion('Feedback', 'Do you wanna give us a Video Feedback ?')
        import video
        tk.messagebox.showinfo('Return', 'Thank you for your response...!')
    else:
        tk.messagebox.askquestion('Feedback', 'Do you wanna give us a Video Feedback ?')
        import video
        tk.messagebox.showinfo('Return', 'Thank you for your response...!')


button1 = tk.Button (root, text='Phoot Booth',command=Photo,bg='brown',fg='white')
canvas1.create_window(130, 450, window=button1)

root.mainloop()
