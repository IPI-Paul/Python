#!/usr/bin/env python3

# Example 8-40
# Displays a button that changes its image at random each time it is pressed
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-20

from tkinter import *                           # get base widget set
from glob import glob                           # filename expansioon list
import demoCheck                                # attache checkbutton demo to me
import random                                   # pick a picture at random
gifdir = '../sourceFiles/images/'                # where to look for GIF/PNG files

def draw():
    name, photo = random.choice(images)
    lbl.config(text=name)
    pix.config(image=photo)

root = Tk()
lbl = Label(root, text='none', bg='blue', fg='magenta')
pix = Button(root, text='Press me', command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)
demoCheck.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)

files = glob(gifdir + '*.gif') + glob(gifdir + '*.png') # GIFs and PNGs for now
images = [(x, PhotoImage(file=x)) for x in files]       # load and hold
print(files)
root.mainloop()