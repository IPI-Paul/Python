#!/usr/bin/env python3

# Example 7-5
# Demonstrates that because some widget methods are exported as functions in 
# tkinter, we can reduce the lines code needed to produce similar results
# Author: Mark Lutz
# Last modified: 

from tkinter import *
Label(text='Hello GUI world!').pack()
mainloop()