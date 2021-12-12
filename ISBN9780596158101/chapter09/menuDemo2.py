#!/usr/bin/env python3

# Example 9-8
# Adds a toolbar to a window. It also demonstrates how to add photo images in 
# menu entries and how to disable entries and give them a grayed-out appearance
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-22

"""
TH8.0 style main window menus
menu/tool bars packed before middle, fill=X (pack first=clip last);
adds photo menu entries; see also: add_checkbutton, add_radiobutton
"""

from tkinter import *                               # get widget classes
from tkinter.messagebox import *                    # get standard dailogs
import sys, os
sys.path.append('..')

class NewMenuDemo(Frame):                           # an extended frame
    
    def __init__(self, parent=None):                # attach to top-level?
        Frame.__init__(self, parent)                # do superclass init
        self.pack(expand=YES, fill=BOTH)
        self.createWidgets()                        # attach frames/widgets
        self.master.title('Toolbars and Menus')     # set window-manager info
        self.master.iconname('tkpython')            # label when inconified
    
    def createWidgets(self):
        self.makeMenuBar()
        self.makeToolBar()
        L = Label(self,  text='Menu and Toolbar Demo')
        L.config(relief=SUNKEN, width=40, height=10, bg='white')
        L.pack(expand=YES, fil=BOTH)
    
    def makeToolBar(self, size=(40, 40)):
        from PIL.ImageTk import PhotoImage, Image   # if jpegs or make new thumbs
        imgdir = r'../sourceFiles/images/'
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        photos = ('py-blue-trans-out.jpg', 'queen-of-hearts.jpg', 'tk.jpg')
        self.toolPhotoObjs = []
        for file in photos:
            imgobj = Image.open(imgdir + file)          # make new thumb
            imgobj.thumbnail(size, Image.ANTIALIAS)      # best downsize filter
            try:
                img = PhotoImage(imgobj)
            except:
                if sys.platform == 'cygwin':
                    from ipi.imageconvert import ImageConvert
                    imgobj = ImageConvert(imgdir + file)
                    img = imgobj.toThumb(size=size, filter=Image.ANTIALIAS)
                    imgobj.remove()
                else:
                    print('Skipping: ', imgdir + file)
            btn = Button(toolbar, image=img, command=self.greeting)
            btn.config(relief=RAISED, bd=2)
            btn.config(width=size[0], height=size[1])
            btn.pack(side=LEFT)
            self.toolPhotoObjs.append((img, imgobj))    #keep a reference
        Button(toolbar, text='Quit', command=self.quit).pack(side=RIGHT)
        Button(toolbar, text='Hello', command=self.greeting).pack(side=LEFT)
    
    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)       # master=top=level window
        self.fileMenu()
        self.editMenu()
        self.imageMenu()
    
    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Open..', command=self.notdone)
        pulldown.add_command(label='Quit..', command=self.quit)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)
        
    def editMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Paste', command=self.notdone)
        pulldown.add_command(label='Spam', command=self.greeting)
        pulldown.add_separator()
        pulldown.add_command(label='Delete', command=self.greeting)
        pulldown.entryconfig(4, state=DISABLED)
        self.menubar.add_cascade(label='Edit', underline=0, menu=pulldown)
    
    def imageMenu(self):
        photoFiles = ('py-blue-trans-out.gif', 'queen-of-hearts.gif', 'tk.gif')
        pulldown = Menu(self.menubar)
        self.photoObjs = []
        for file in photoFiles:
            img = PhotoImage(file='../sourceFiles/images/' + file)
            pulldown.add_command(image=img, command=self.notdone)
            self.photoObjs.append(img)                  # keep a reference
        self.menubar.add_cascade(label='Image', underline=0, menu=pulldown)
    
    def greeting(self):
        showinfo('greeting', 'Greetings')
        
    def notdone(self):
        showerror('Not implemented', 'Not yet available')
        
    def quit(self):
        if askyesno('Verifying quit', 'Are you sure you want to quit?'):
            Frame.quit(self)

if __name__ == '__main__': NewMenuDemo().mainloop()     # if I'm run as a script