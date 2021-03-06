#!/usr/bin/env python3

# Example 8-18
# Combines labels, entries, and frames to achieve a multiple-input display
# Author: Mark Lutz
# Last modified: 

"""
use Entry widgets directly
lay out by rows with fixed-width labels: this and grid are best for forms
"""

from tkinter import *
from quitter import Quitter

fields = 'Name', 'Job', 'Pay'

def fetch(entries):
    for entry in entries:
        print('input => "%s"' % entry.get())                # get text

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)                                   # make a new row
        lab = Label(row, width=5, text=field)               # add label
        ent = Entry(row)
        row.pack(side=TOP, fill=X)                          # pack row on top
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)            # grow horizontally
        entries.append(ent)
    return entries

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event: fetch(ents)))
    Button(root, text='Fetch', command=(lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()