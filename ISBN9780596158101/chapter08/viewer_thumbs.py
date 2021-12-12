#!/usr/bin/env python3

# Example 8-45
# Generates thumbnail images using PIL and displays them on buttons which open 
# the corresponding original image when clicked.
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2018-11-21

"""
display all images in a directory as thumbnail image buttons that display the 
full image when clicked; requires PIL for JPEGs and thumbnail image creation; 
to do: add scrolling if too many thumbs wor window!
"""

import os, sys, math
from tkinter import * 
from PIL import Image                       # <== required for thumbs
from PIL.ImageTk import PhotoImage          # <== required for JPEG display
sys.path.append('..')

def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    """
    get thumbnial images for all images in a directory; for each image, create
     and save a new thumb, or load and return an existing thumb; makes thumb dir 
     if needed; returns a list of (image filename, thumb image object): 
     caller can also run listdir on thumb dir to load; on bad file types may 
     raise an IOError, or other; caveat: could also check file timestamps;
    """
    thumbdir = os.path.join(imgdir, subdir)
    if not os.path.exists(thumbdir):
        os.mkdir(thumbdir)
    
    thumbs = []
    for imgfile in os.listdir(imgdir):
        thumbpath = os.path.join(thumbdir, imgfile)
        if os.path.exists(thumbpath):
            try:
                thumbobj = Image.open(thumbpath)            # use already created
                thumbs.append((imgfile, thumbobj))
            except:
                print('Skipping: ', thumbpath)
        else:
            print('making', thumbpath)
            imgpath = os.path.join(imgdir, imgfile)
            try:
                imgobj = Image.open(imgpath)            # make new thumb
                imgobj.thumbnail(size, Image.ANTIALIAS) # best downsize filter
                imgobj.save(thumbpath)                  # type via ext or passed
                thumbs.append((imgfile, imgobj))
            except:
                print('Skipping: ', imgpath)
    return thumbs

class ViewOne(Toplevel):
    """
    open a single image in a pop-up window when created; photoimage object must 
    be saved: images are erased if object is reclaimed;
    """
    
    def __init__(self, imgdir, imgfile):
        Toplevel.__init__(self)
        self.title(imgfile)
        imgpath = os.path.join(imgdir, imgfile)
        try:
            imgobj = PhotoImage(file=imgpath)
        except:
            if sys.platform == 'cygwin':
                from ipi.imageconvert import ImageConvert
                img = ImageConvert(imgpath)
                imgobj = img.toPNG()
                img.remove()
            else:
                print('Skipping: ', imgfile)
        Label(self, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height())     # size in pixels
        self.savephoto = imgobj                             # keep reference on me
        
def viewer(imgdir, kind=Toplevel, cols=None):
    """
    make thumb links window for an image directory: one thumb button per 
    image: use kind=Tk to show in main app window, or Frame container (pack);
    imgfile differs per loop: must save with a default; photoimage objs must 
    be saved; erased if reclaimed; packed row frames (versus grids, 
    fixed-sizes, canvas);
    """
    win = kind()
    win.title('Viewer: ' + imgdir)
    quit = Button(win, text='Quit', command=win.quit, bg='beige') # pack first
    quit.pack(fill=X, side=BOTTOM)                                # so clip last
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))           # fixed or N x N
    
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        row = Frame(win)
        row.pack(fill=BOTH)
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
            link = Button(row, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)
    return win, savephotos

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or '../sourceFiles/images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()