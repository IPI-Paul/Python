#!/usr/bin/env python3

# Example 7-3
# Makes all tkinter imports more explicit by grabbing the whole module and 
# prefixing all of its names with the moule's name
# Author: Mark Lutz
# Last modified: 

import tkinter
widget = tkinter.Label(None, text='Hello GUI world!')
widget.pack()
widget.mainloop()