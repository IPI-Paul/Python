#!/usr/bin/env python3

# Example 8-43
# Uses PIL module's PhotoImage to display a single image by attaching it to a 
# label in the main application window
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-21

"""
show one image with PIL photo replacement object
handles many more image types; install PIL firts: placed in Lib\site-packages
"""

import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage              # <== use PIL replacement class
sys.path.append('..')
#                                                 rest of code unchanged
imgdir = '../sourceFiles/images/'
imgfile = 'queen-of-hearts.jpg'                 # does gif, jpg, png, tiff, etc
if len(sys.argv) > 1:
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
try:
    imgobj = PhotoImage(file=imgpath)        # now JPEGs work!
    Label(win, image=imgobj).pack()
    win.mainloop()
    print(imgobj.width(), imgobj.height())   # show size in pixels on exit 
except:
    if sys.platform == 'cygwin':
        from ipi.imageconvert import ImageConvert
        imgobj = ImageConvert(imgpath)          # now JPEGs work in Cygwin!
        Label(win, image=imgobj.toPNG()).pack()
        imgobj.remove()
        print(imgobj.width(), imgobj.height())  # show size in pixels before exit 
        win.mainloop()        