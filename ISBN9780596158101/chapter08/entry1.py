#!/usr/bin/env python3

# Example 8-17
# Builds an input window with an Entry widget
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-18

from tkinter import *
from quitter import Quitter

def fetch():
    print('Input => %s' % ent.get())                    # get text

def clear(event):
    ent.delete(0, END)
    
root = Tk()
ent = Entry(root)
ent.insert(0, 'Type words here')                        # set text
ent.pack(side=TOP, fill=X)                              # grow horizontally

ent.focus()                                             # save a click
ent.bind('<Return>', (lambda event: fetch()))           # on enter key
ent.bind('<Button-2>', clear)
ent.bind('<Button-3>', clear)
btn = Button(root, text='Fetch', command=fetch)         # and on button
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()