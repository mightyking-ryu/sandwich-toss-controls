from tkinter import *
from PIL import Image
from PIL import ImageTk

#Define the tkinter instance
win= Toplevel()
win.title("Rounded Button")

#Define the size of the tkinter frame
win.geometry("1000x1000")
win.config(bg="black")

#Define the working of the button

def my_command():
   text.config(text= "You have clicked Me...")

#Import the image using PhotoImage function
click_btn= PhotoImage(file='clickme.png')

#Let us create a label for button event
img_label= Label(image=click_btn)

im = Image.open("clickme.png")
resized = im.resize((200, 100), Image.ANTIALIAS)

def png_change_bg(im, fill_color):

    im = im.convert("RGBA")   # it had mode P after DL it from OP
    if im.mode in ('RGBA', 'LA'):
        background = Image.new(im.mode[:-1], im.size, fill_color)
        background.paste(im, im.split()[-1]) # omit transparency
        im = background
        im.convert("RGB")
        
    im = ImageTk.PhotoImage(im)
    return im

#Let us create a dummy button and pass the image
button= Button(win, image=im,command= my_command,
borderwidth=0)
button.config(background="black")
button.pack(pady=30)


text= Label(win, text= "")
text.pack(pady=30)

win.mainloop()