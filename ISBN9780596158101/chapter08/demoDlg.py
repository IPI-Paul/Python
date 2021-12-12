#!/usr/bin/env python3

# Example 8-9
# Generates buttons for all of the table entries in Example 8-8 then uses its keys
# as button labels and its values as button callback handlers
# Author: Mark Lutz
# Last modified: 

'create a bar of simple buttons that launch dialog demos'

from tkinter import *                           # get base widget
from dialogTable import demos                   # button callback handlers
from quitter import Quitter                     # attach a quit object to me

class Demo(Frame):
    
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Basic demos').pack()
        for (key, value) in sorted(demos.items()):
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)

if __name__ == '__main__': Demo().mainloop()