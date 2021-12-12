#!/usr/bin/env python3

# Example 9-15
# Is a mutation of the last chapter's code, which displays thumbnails in a 
# scrollable canvas.
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-24

"""
image viewer extension: uses fixed-size thumbnail buttons for uniform layout, and 
adds scrolling for large image sets by displaying thumbs in a canvas widget with
scroll bars; requires PIL to view image formats such as JPEG, reuses thumbs maker
and single photo viewer in viewer_thumbs.py; caveat/to do: this could also scroll
popped-up images that are too large for the screen, and are cropped on Windows as
is; see PyPhoto later in Chapter 11 for a much more complete version
"""

import sys, math, os
from tkinter import *
from PIL.ImageTk import PhotoImage
sys.path.append('..')
from chapter08.viewer_thumbs import makeThumbs, ViewOne

def viewer(imgdir, kind=Toplevel, numcols=None, height=300, width=300):
    """
    use fixed-size buttons, scrollable canvas:
    sets scrollable (full) size, and places thumbs ar absolute x, y
    coordinates in canvas; caveat: assumes all thumbs are same size
    """
    win = kind()
    win.title('Simple viewer: ' + imgdir)
    quit = Button(win, text='Quit', command=win.quit, bg='beige')
    quit.pack(side=BOTTOM, fill=X)
    
    canvas =Canvas(win, borderwidth=0)
    vbar = Scrollbar(win)
    hbar = Scrollbar(win, orient='horizontal')
    
    vbar.pack(side=RIGHT, fill=Y)                   # pack canvas after bars
    hbar.pack(side=BOTTOM, fill=X)                  # so clipped first)
    canvas.pack(side=TOP, fill=BOTH, expand=YES)
    
    vbar.config(command=canvas.yview)               # call on scroll
    hbar.config(command=canvas.xview)
    canvas.config(yscrollcommand=vbar.set)          # call on canvas move
    canvas.config(xscrollcommand=hbar.set)
    canvas.config(height=height, width=width)       # init viewable area size
    #                                                 changes if user resizes
    thumbs = makeThumbs(imgdir)                     # [(imgfile, imgobj)]
    numthumbs = len(thumbs)
    if not numcols:
        numcols = int(math.ceil(math.sqrt(numthumbs)))  # fixed or N x N
    numrows = int(math.ceil(numthumbs / numcols))       # 3.x true div
    
    linksize = max(x.size for _, x in thumbs)[1]        # (width, height)
    #linksize = max(thumbs[0][1].size)                  # (width, height)
    fullsize = (0, 0,                                   # upper left X, Y
                (linksize * numcols), (linksize * numrows)) # lower right X, Y
    canvas.config(scrollregion=fullsize)                # scrollable area size
    
    rowpos = 0
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:numcols], thumbs[numcols:]
        colpos = 0
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
            link = Button(canvas, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler, width=linksize, height=linksize)
            link.pack(side=LEFT, expand=YES)
            canvas.create_window(colpos, rowpos, anchor=NW, 
                                 window=link, width=linksize, height=linksize)
            colpos += linksize
            savephotos.append(photo)
        rowpos += linksize
    return win, savephotos

if __name__ == '__main__':
    imgdir = '../sourceFiles/images' if len(sys.argv) < 2 else sys.argv[1]
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()
