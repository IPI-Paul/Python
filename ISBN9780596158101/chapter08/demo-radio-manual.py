#!/usr/bin/env python3

# Example 8-27
# Implements a single-selection model without variables, by manually selecting 
# and deselecting widgets in the group, in a callback handler of its own
# Author: Mark Lutz
# Last modified: 

"""
radio buttons, the hard way *(without variables)
note that deselect for radio buttons simply sets the button's associated value 
to a null string, so we either need to still give buttons unique values, or use 
checkbuttons here instead;
"""

from tkinter import *

state = ''
buttons = []

def onPress(i):
    global state
    state =i
    for btn in buttons:
        btn.deselect()
    buttons[i].select()

root = Tk()
for i in range(10):
    rad = Radiobutton(root, text=str(i),
                      value=str(i), command=(lambda i=i: onPress(i)))
    rad.pack(side=LEFT)
    buttons.append(rad)

onPress(0)                                      # select first initially
root.mainloop()
print(state)                                    # show state on exit