#!/usr/bin/env python3

# Example 11-7
# This was the initial slideshow implementation; it opens images, displays photos,
# and cycles through a slideshow
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-01-18

"""
################################################################################
SlideShow: a simple photo image slideshow in Python/tkinter; the base feature 
set coded here can be extended in subclasses;
################################################################################
"""

from tkinter import *
from glob import glob
from tkinter.messagebox import askyesno
from tkinter.filedialog import askopenfilename
import random
Size = (450, 450)  # canvas height, width at startup and slideshow start
import os, sys
sys.path.append('..')
from ipi.imageconvert import ImageConvert

imageTypes = [('Bmp files', '.bmp'),    # added support using PIL
              ('Gif files', '.gif'),    # for file open dialog
              ('Jpg files', '.jpg'),    # plus jpg
              ('Pgm files', '.pgm'),    # plus bitmaps with bitmapImage
              ('Png files', '.png'),    # plus png
              ('Ppm files', '.ppm'),    # plus jpg with Tk patch,
              ('All files', '*')]

class SlideShow(Frame):
    def __init__(self, parent=None, picdir='.', msecs=3000, size=Size, **args):
        Frame.__init__(self, parent, **args)
        self.size = size
        self.makeWidgets()
        self.pack(expand=YES, fill=BOTH)
        self.opens = picdir
        files = []
        for label, ext in imageTypes[:-1]:
            files = files + glob('%s/*%s' % (picdir, ext))
        # self.images = [(x, PhotoImage(file=x)) for x in files]
        self.images = [(x, self.getImage(name=x)) for x in files]        
        self.msecs = msecs
        self.beep = True
        self.drawn = None
    
    def getImage(self, name=None):
        try:
            img = PhotoImage(file=name)
        except:
            imgpath = os.path.join(os.path.dirname(name), 'tmp')
            if not os.path.exists(imgpath):
                os.mkdir(imgpath)
            imgpil = ImageConvert(name, imgTmp=imgpath+'/tmp')
            img = imgpil.toPNG()
            imgpil.remove()                
        return img
    
    def makeWidgets(self):
        height, width = self.size
        self.canvas = Canvas(self, bg='white', height=height, width=width)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        self.onoff = Button(self, text='Start', command=self.onStart)
        self.onoff.pack(fill=X)
        Button(self, text='Open', command=self.onOpen).pack(fill=X)
        Button(self, text='Beep', command=self.onBeep).pack(fill=X)
        Button(self, text='Quit', command=self.onQuit).pack(fill=X)
    
    def onStart(self):
        self.loop = True
        self.onoff.config(text='Stop', command=self.onStop)
        self.canvas.config(height=self.size[0], width=self.size[1])
        self.onTimer()
    
    def onStop(self):
        self.loop = False
        self.onoff.config(text='Start', command=self.onStart)
    
    def onOpen(self):
        self.onStop()
        name = askopenfilename(initialdir=self.opens, filetypes=imageTypes)
        if name:
            if self.drawn: self.canvas.delete(self.drawn)
            try:
                img = PhotoImage(file=name)
            except:
                imgpath = os.path.join(os.path.dirname(name), 'tmp')
                if not os.path.exists(imgpath):
                    os.mkdir(imgpath)
                imgpil = ImageConvert(name, imgTmp=imgpath+'/tmp')
                img = imgpil.toPNG()
                imgpil.remove()                
            self.canvas.config(height=img.height(), width=img.width())
            self.drawn = self.canvas.create_image(2, 2, image=img, anchor=NW)
            self.image = name, img
    
    def onQuit(self):
        self.onStop()
        self.update()
        if askyesno('PyEdit', 'Really quit now?'):
            self.quit()
    
    def onBeep(self):
        self.beep = not self.beep           # toggle, or use ^ 1
    
    def onTimer(self):
        if self.loop:
            self.drawNext()
            self.after(self.msecs, self.onTimer)
    
    def drawNext(self):
        if self.drawn: self.canvas.delete(self.drawn)
        name, img = random.choice(self.images)
        self.drawn = self.canvas.create_image(2, 2, image=img, anchor=NW)
        self.image = name, img
        if self.beep: self.bell()
        self.canvas.update()
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        picdir = sys.argv[1]
    else:
        picdir = '../sourceFiles/images'
    root =Tk()
    root.title('PyView 1.2')
    root.iconname('PyView')
    Label(root, text='Python Slide Show Viewer').pack()
    SlideShow(root, picdir=picdir, bd=3, relief=SUNKEN)
    root.mainloop()