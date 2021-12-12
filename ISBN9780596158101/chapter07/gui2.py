#!/usr/bin/env python3

# Example 7-10
# Demonstrates a responsive interface
# Author: Mark Lutz
# Last modified: 

import sys
from tkinter import *
widget = Button(None, text='Hello GUI world', command=sys.exit)
widget.pack()
widget.mainloop()