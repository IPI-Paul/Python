#!/usr/bin/env python3

# Example 7-17
# Displays a Label and 2 button widgets in a window
# Author: Mark Lutz
# Last modified: 

from tkinter import *

def greeting():
    print('Hello stdout world!...')

win = Frame()
win.pack()
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

win.mainloop()