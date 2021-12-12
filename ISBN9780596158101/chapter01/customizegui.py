#!/usr/bin/env python3

# Example 1-27
# Customsies the reply method to do something unique
# Author: Mark Lutz
# Last modified: 

from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):                     # inherit init
    def reply(self):                        # replace reply
        showinfo(title='popup', message='Ouch!')

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()