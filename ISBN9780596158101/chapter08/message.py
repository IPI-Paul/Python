#!/usr/bin/env python3

# Example 8-16
# Illustrates the tkinterMessage basics, and demonstrates how Message reacts to 
# horizontal stretching with fill and expand
# Author: Mark Lutz
# Last modified: 

from tkinter import *
msg = Message(text="Oh bye the way, which one's Pink?")
msg.config(bg='pink', font=('times', 16, 'italic'))
msg.pack(fill=X, expand=YES)
mainloop()