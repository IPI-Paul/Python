#!/usr/bin/env python3

# Example 19-18
# Customizes the simple calculator's constructor to add extra widgets
# Author: Mark Lutz
# Last modified: 

from tkinter import *
from calc0 import CalcGui

class Inner(CalcGui):                                       # extend GUI
    def __init__(self):
        CalcGui.__init__(self)
        Label(self, text='Calc Subclass').pack()            # add after
        Button(self, text='Quit', command=self.quit).pack() # top implied

Inner().mainloop()