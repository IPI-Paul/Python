#!/usr/bin/env python3

# Example 7-8
# Demonstrates that widget options can be set after construction by calling the 
# widget config method
# Author: Mark Lutz
# Last modified: 

from tkinter import *
root = Tk()
widget = Label(root)
widget.config(text='Hello GUI world!')
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('gui1g.py')
root.mainloop()