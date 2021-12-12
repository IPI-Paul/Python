#!/usr/bin/env python3

# Example 8-38
# Uses tkinter Canvas widget's general drawing surface to display a picture
# Author: Mark Lutz
# Last modified: 

gifdir = '../sourceFiles/images/'
from tkinter import *
win = Tk()
img = PhotoImage(file=gifdir + 'py-blue-trans-out.png')
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW)                # x, y coordinates
win.mainloop()