#!/usr/bin/env python3

# Example 9-20
# Puts both the packed and the gridded widgets together on the same window, but 
# only by isolating each in its own Frame container widget
# Author: Mark Lutz
# Last modified: 

"""
build pack and grid forms on different frames in same window; can't grid and 
pack in same parent container (e.g., root window) but can mix in same window if 
done in different parent frames
"""

from tkinter import *
from grid2 import gridbox, packbox

root = Tk()

Label(root, text='Grid:').pack()
frm = Frame(root, bd=5, relief=RAISED)
frm.pack(padx=5, pady=5)
gridbox(frm)

Label(root, text='Pack:').pack()
frm = Frame(root, bd=5, relief=RAISED)
frm.pack(padx=5, pady=5)
packbox(frm)

Button(root, text='Quit', command=root.quit).pack()
mainloop()