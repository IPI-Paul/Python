#!/usr/bin/env python3

# Example 7-2
# Displays a 'Hello World' message in a window without the initial shell window
# Author: Mark Lutz
# Last modified: 

from  tkinter import Label                          # get a widgt object
widget = Label(None, text='Hello GUI World!')       # make on
widget.pack()                                       # arrange it
widget.mainloop()                                   # start event loop