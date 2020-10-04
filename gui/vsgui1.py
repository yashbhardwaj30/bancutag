from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from tkinter import filedialog
from tkinter import Frame

window = Tk()
#window.resizable(0,0)
width_of_window=1020
height_of_window=520
width_val=window.winfo_screenwidth()
height_val=window.winfo_screenheight()
x_cord=(width_val/2)-(width_of_window/2)
y_cord=(height_val/2)-(height_of_window/2)
#window.title("Space App")
window.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_cord,y_cord))
#window.configure(bg='black')

load=Image.open('back1.jpg')
render=ImageTk.PhotoImage(load)
img=Label(window,image=render,bg='#040428')
img.place(x=0,y=0)

def change(e):
    butt_exit=PhotoImage(file="b.png")
    butt_label.config(image=butt_exit)
    butt_label.image= butt_exit

def change_back(e):
    butt_exit=PhotoImage(file="b1.png")
    butt_label.config(image=butt_exit)
    butt_label.image= butt_exit



logo=PhotoImage(file="logo1.png")
logo_label=Label(window,image=logo,bg='#040428')
logo_label.pack(side=TOP)

icon=PhotoImage(file="icon.png")
icon_label=Label(window,image=icon,bg='#000120')
icon_label.place(x=0,y=0)

butt_exit=PhotoImage(file="b1.png")
butt_label=Button(window,image=butt_exit,bg='#020025',bd=0,command=window.destroy)
butt_label.pack(side=BOTTOM)

frame = Frame(window, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 150 # Processing image for dysplaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = PhotoImage(img)
    file_name = image_data.split('/')
    panel = Label(frame, text= str(file_name[len(file_name)-1]).upper()).pack()
    panel_image = Label(frame, image=img).pack()



chose_image =Button(window, text='Choose Image',padx=35, pady=10,fg="white", bg="grey", command=load_img)

chose_image.pack(side=LEFT)

butt_label.bind("<Enter>",change)
butt_label.bind("<Leave>",change_back)

window.overrideredirect(1)

window.mainloop()