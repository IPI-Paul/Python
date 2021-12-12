#!/usr/bin/env python3

# Example 8-7
# Implements an attachable Quit button that uses standard dialogs to verify the 
# quit request. Because it's a class, it can be attached and reused in any 
# application that needs a verifying Quit button
# Author: Mark Lutz
# Last modified: 

"""
a Quit button that verifies exit requests; to reuse, attach an instance to other
GUIs, and re-pack as desired
"""

from tkinter import *                               # get widget class
from tkinter.messagebox import askokcancel          # get canned std dialog

class Quitter(Frame):                               # subclass our GUI
    
    def __init__(self, parent=None):                # constructor method
        Frame.__init__(self, parent)
        try:
            self.pack()
        except:
            pass
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)
        
    def quit(self):
        ans = askokcancel('Verify exit', 'Really quit?')
        if ans: Frame.quit(self)

if __name__ == '__main__': Quitter().mainloop()