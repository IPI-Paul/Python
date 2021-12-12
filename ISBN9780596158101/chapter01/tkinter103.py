#!/usr/bin/env python3

# Example 1-28
# Show how to input data from the user in an Entry widget and display it in a 
# pop-up dialog. The lambda it uses defers the call to the reply function so that
# inputs can be passed in
# Author: Mark Lutz
# Last modified: 

from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)
    
top = Tk()
top.title('Echo')
img = '../sourceFiles/images/py-blue-trans-out.ico'
if sys.platform[:3] == 'cyg':
    top.iconphoto(True, PhotoImage(file=img.replace('ico', 'png')))
else:
    top.iconbitmap(img)                                 

Label(top, text='Enter your name:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)

top.mainloop()