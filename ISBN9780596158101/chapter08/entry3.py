#!/usr/bin/env python3

# Example 8-20
# Demonstrates how a StringVar class instance can be associated with an Entry 
# field. Variables tied to widgets are instances of variable classes in the 
# tkinter module library (StringVar, IntVar, and DoubleVar).
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-18

"""
use StringVar variables
lay out by columns: this might not align horizontally everywhere (see entry2)
"""

from tkinter import *
from quitter import Quitter

fields = 'Name', 'Job', 'Pay'

def fetch(variables):
    for variable in variables:
        print('Input => "%s"' % variable.get())             # get from var

def makeform(root, fields):
    form = Frame(root)                                      # make outer frame
    left = Frame(form)                                      # make two columns
    rite = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)               # grow horizontally
    
    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)              # add to columns
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)                          # grow horizontally
        var = StringVar()
        ent.config(textvariable=var)                        # link field to var
        var.set('enter here')
        variables.append(var)
        root.bind('<Button-2>', (lambda event: delEntry(event)))
        root.bind('<Button-3>', (lambda event: delEntry(event)))
    return variables

def delEntry(ent):
    ent.widget.delete(0, END)

if __name__ == '__main__':
    root =Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()