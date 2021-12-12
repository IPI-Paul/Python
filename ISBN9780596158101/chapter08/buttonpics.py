#!/usr/bin/env python3

# Example 8-41
# ReWrites Example 8-40 as a class
# Author: Mark Lutz
# Last modified: 

from tkinter import *                       # get base widget set
from glob import glob                       # filename expansion list
import demoCheck                            # attach check button example to me
import random                               # pick a picture at random
gifdir = '../sourceFiles/images/'           # default dir to load GIF/PNG Files

class ButtonPicsDemo(Frame):
    
    def __init__(self, gifdir=gifdir, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.lbl = Label(self, text='none', bg='blue', fg='magenta')
        self.pix = Button(self, text='Press me', command=self.draw, bg='white')
        self.lbl.pack(fill=BOTH)
        self.pix.pack(pady=10)
        demoCheck.Demo(self, relief=SUNKEN, bd=2).pack(fill=BOTH)
        files = glob(gifdir + '*.gif') + glob(gifdir + '*.png')
        self.images = [(x, PhotoImage(file=x)) for x in files]
        print(files)
    
    def draw(self):
        name, photo = random.choice(self.images)
        self.lbl.config(text=name)
        self.pix.config(image=photo)

if __name__ == '__main__': ButtonPicsDemo().mainloop()