#!/usr/bin/env python3

# Example 8-44
# Opens a new Toplevel pop-up window for each image in a directory (given as a 
# command-line argument or a default), taking care to skip nonimage files be 
# catching exceptions
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-21

"""
desplay all images in a directory in pop-up windows
GIFs work in basic tkinter, but JPEGs will be skipped without PIL
"""

import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage          # <== required for JPEG and others
sys.path.append('..')

imgdir = '../sourceFIles/images/'
if len(sys.argv) > 1: imgdir = sys.argv[1]
imgfiles = os.listdir(imgdir)               # does not include directory prefix

main = Tk()
main.title('Viewer')
quit = Button(main, text='Quit all', command=main.quit, font=('courier', 25))
quit.pack()
savephotos = []

for imgfile in imgfiles:
    imgpath = os.path.join(imgdir, imgfile)
    win = Toplevel()
    win.title(imgfile)
    if not sys.platform == 'cygwin':
        try:
            imgobj = PhotoImage(file=imgpath)
            Label(win, image=imgobj).pack()
            print(imgpath, imgobj.width(), imgobj.height()) # size in pixels
            savephotos.append(imgobj)                       # keep a reference
        except:
            errmsg = 'skipping %s\n%s' % (imgfile, sys.exc_info()[1])
            Label(win, text=errmsg).pack()
    else:
        try:
            from ipi.imageconvert import ImageConvert
            imgobj = ImageConvert(imgpath)
            Label(win, image=imgobj.toPNG()).pack()
            print(imgpath, imgobj.width(), imgobj.height()) # size in pixels
            savephotos.append(imgobj)                       # keep a reference
            imgobj.remove()
        except:
            errmsg = 'skipping %s\n%s' % (imgfile, sys.exc_info()[1])
            Label(win, text=errmsg).pack()

mainloop()