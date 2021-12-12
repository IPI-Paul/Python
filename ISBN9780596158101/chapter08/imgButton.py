#!/usr/bin/env python3

# Example 8-37
# Uses tkinter PhotoImage or BitmapImage objects to throw a picture up on a 
# button
# Author: Mark Lutz
# Last modified: 

gifdir = '../sourceFiles/images/'
from tkinter import *
win = Tk()
igm = PhotoImage(file=gifdir + 'tk.gif')
Button(win, image=igm).pack()
win.mainloop()