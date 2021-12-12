#!/usr/bin/env python3

# Example 8-48
# Sets the height and width of each button to match the maximum dimension of the 
# thumbnail icon
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-21

"""
use fixed size for thumbnails, so align regularly; size taken from image objec,
assume all same max; this is essentially what file selection GUIs do
"""

import sys, math, os
from tkinter import *
from PIL.ImageTk import PhotoImage
from viewer_thumbs import makeThumbs, ViewOne
sys.path.append('..')

def viewer(imgdir, kind=Toplevel, cols=None):
    """
    custom version that lays out which fixed-size buttons
    """
    win = kind()
    win.title('Viewer: ' + imgdir)
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))      # fixed or N x N
    
    savephotos = []
    size = max(x.size for _, x in thumbs)[1]                # width, height
    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        row = Frame(win)
        row.pack(fill=BOTH)
        for (imgfile, imgobj) in thumbsrow:
            #size = max(imgobj.size)                         # width, height
            try:
                photo = PhotoImage(imgobj)
            except:
                if sys.platform == 'cygwin':
                    from ipi.imageconvert import ImageConvert
                    img = ImageConvert(imgobj.filename)
                    photo = img.toPNG()
                    img.remove()            
                else:
                    print('Skipping: ', imgobj.filename)
            link = Button(row, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler, width=size, height=size)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)
            
    Button(win, text='Quit', command=win.quit, bg='beige').pack(fill=X)
    return win, savephotos

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or '../sourceFiles/images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()