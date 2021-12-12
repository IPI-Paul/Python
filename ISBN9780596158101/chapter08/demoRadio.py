#!/usr/bin/env python3

# Example 8-25
# Demonstrates radio buttons basics
# Author: Mark Lutz
# Last modified: 

'create a group of radio buttons that launch dialog demos'

from tkinter import *                           # get base widget
from dialogTable import demos                   # button callback handlers
from quitter import Quitter                     # attach a quit object tom 'me'

class Demo(Frame):
    
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Radio Demos').pack(side=TOP)
        self.var = StringVar()
        for key in sorted(demos):
            Radiobutton(self, text=key,
                        command=self.onPress,
                        variable=self.var,
                        value=key).pack(anchor=NW)
        self.var.set(key)                           # select last to start
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)
    
    def onPress(self):
        pick = self.var.get()
        print('you pressed', pick)
        print('result:', demos[pick]())
    
    def report(self):
        print(self.var.get())

if __name__ == '__main__': Demo().mainloop()