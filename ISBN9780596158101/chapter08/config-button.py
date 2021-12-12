#!/usr/bin/env python3

# Example 8-2
# Illustrates extra settings like (border and relief; Cursor; State; and Padding)
# by configuring a custom button and changing the mouse pointer when it is 
# positioned above it
# Author: Mark Lutz
# Last modified: 

from tkinter import *

widget = Button(text='Spam', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=8, relief=RAISED)
widget.config(bg='dark green', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
mainloop()