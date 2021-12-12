#!/usr/bin/env python3

# Example 7-25
# Illustrates that standalone classes are not quite plug-and-play compatible with 
# real widgets objects. The configuration calls made in Example 7-21 for the 
# Frame subclass fail here
# Author: Mark Lutz
# Last modified: 

from tkinter import *
from gui7 import HelloPackage           # or get from gui7c--__getaatr__ added

frm = Frame()
frm.pack()
Label(frm, text='hello').pack()

part = HelloPackage(frm)
try:
    part.pack(side=RIGHT)               # FAILS!--need part.top.pack(side=RIGHT)
except Exception as e:
    print(e)
    quit()
    
frm.mainloop()