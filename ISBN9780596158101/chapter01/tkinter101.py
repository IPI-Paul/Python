#!/usr/bin/env python3

# Example 1-24
# Implements a GUI with a button that actually responds to a user each time it 
# is pressed
# Author: Mark Lutz
# Last modified: 

from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Button pressed')
    
window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()