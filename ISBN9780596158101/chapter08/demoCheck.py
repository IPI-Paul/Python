#!/usr/bin/env python3

# Example 8-22
# Creates the set of five Checkbuttons. It also adds a button that dumps the 
# current state of all the Checkbuttons and attaches an instance of the verifying
# Quitter button
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-19

'create a bar of check buttons that run dialog demos'

from tkinter import *                   # get base widget set
from dialogTable import demos           # get canned dialogs
from quitter import Quitter             # attach a quitter object to "me"

class Demo(Frame):
    
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        Label(self, text='Check demos').pack()
        self.vars = []
        for key in sorted(demos):
            var = IntVar()
            Checkbutton(self,
                        text=key,
                        variable=var,
                        command=(lambda x=var, y=key: self.test(x, y))
                        ).pack(side=LEFT)
            self.vars.append(var)
    
    def report(self):
        for var in self.vars:
            print(var.get(), end=' ')       # current toggle settings: 1 or 0
        print()
    
    def test(self, var, key):
        if var.get() == 1:
            demos[key]()
    
    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        Button(frm, text='State', command=self.report).pack(fill=X)
        Quitter(frm).pack(fill=X)

if __name__ == '__main__':  Demo().mainloop()