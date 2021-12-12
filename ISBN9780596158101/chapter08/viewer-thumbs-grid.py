#!/usr/bin/env python3

# Example 8-47
# Positions buttons in a row/column grid using the tkinter grid geometry manager
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-21

"""
same as viewer_thumbs, but uses the grid geometry manager to try to achieve a 
more uniform layout; can generally achieve the same with frames and pack if 
buttons are all fixed and uniform in size
"""

import sys, math, os
from tkinter import *
from PIL.ImageTk import PhotoImage
from viewer_thumbs import makeThumbs, ViewOne
sys.path.append('..')

def viewer(imgdir, kind=Toplevel, cols=None):
    """
    custom version that uses gridding
    """
    win = kind()
    win.title('Viewer: ' + imgdir)
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))           # fixed or N x N
    
    rownum = 0
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        colnum = 0
        for (imgfile, imgobj) in thumbsrow:
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
            link = Button(win, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler)
            link.grid(row=rownum, column=colnum)
            savephotos.append(photo)
            colnum += 1
        rownum += 1
    Button(win, text='Quit', command=win.quit).grid(columnspan=cols, stick=EW)
    return win, savephotos

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or '../sourceFiles/images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()