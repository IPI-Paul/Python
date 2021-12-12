#!/usr/bin/env python3

# Example by IPI-Paul.
# Adds other image formats to Python using Pillow modules. Converts to images to 
# other formats and saves them in the Cygwin /tmp or specified folder as tmp.png 
# or specified image folder/name/extension
# Author: Paul I Ighofose
# Last modified: 2018-11-19

"""
Converts to images to other formats and saves them in the Cygwin /tmp or specified 
folder as tmp.png or specified image folder/name/extension
"""

import os
from tkinter import PhotoImage
from PIL import Image
from glob import glob

class ImageConvert:
    
    def __init__(self, file, imgTmp='/tmp/tmp', imgExt='.png', thumb=False,
                 toPath=False, resize=False):
        self.file = file
        self.imgTmp = imgTmp
        self.imgExt = imgExt
        self.tmpFile = os.path.join(imgTmp, imgExt)
        self.thumb = thumb
        self.resize = resize
        self.toPath = toPath
        
    def height(self):
        return self.imgobj.height()

    def width(self):
        return self.imgobj.width()
    
    def checkName(self):
        files = []
        files += glob(self.imgTmp + '*' + self.imgExt)
        mx = 0 if files == [] else int(max(x.replace(self.imgTmp,'').replace(
            self.imgExt, '') for x in files))
        for i in range(mx + 100):
            file = self.imgTmp + str(i) + self.imgExt
            if not os.path.exists(file):
                self.tmpFile = file
                return self.convert(file)
            
    def convert(self, imgTmp):
        if self.resize == True:
            Image.open(self.file).convert(
                'RGB').resize(self.size, self.filter).save(imgTmp)
        else:
            Image.open(self.file).convert('RGB').save(imgTmp)
            if self.thumb == True:
                from PIL.ImageTk import Image as TkImage
                img = TkImage.open(imgTmp)
                img.thumbnail(self.size, self.filter)
                img.save(imgTmp)
        if not self.toPath:
            self.imgobj = PhotoImage(file=imgTmp)
            self.imgobj.size = (self.imgobj.width(), self.imgobj.height())
            return self.imgobj
        else:
            return imgTmp
    
    def remove(self):
        os.remove(self.tmpFile)    
    
    def resizeTo(self, size=(100, 100), filter=Image.BICUBIC):
        self.resize = True
        self.size = size
        self.filter = filter
        return self.checkName()
    
    def saveAs(self, file, ext, parent, canvas):
        filename = os.path.splitext(file)[0] + ext
        try:
            from PIL import ImageGrab
            x = parent.winfo_x() + 8
            y = parent.winfo_y() + 30
            x1 = x + parent.winfo_width()
            y1 = y + parent.winfo_height()
            img = ImageGrab.grab().crop((x, y, x1, y1))
            img.save(filename, subsampling=0, quality=100)
        except:
            canvas.postscript(file=file)
            img = Image.open(file)
            img.save(filename, subsampling=0, quality=100)
            os.remove(file)

    def toBMP(self):
        self.imgExt = '.bmp'
        return self.checkName()    
        
    def toGIF(self):
        self.imgExt = '.gif'
        return self.checkName()        
        
    def toICO(self):
        self.imgExt = '.ico'
        return self.checkName()
        
    def toJPG(self):
        self.imgExt = '.jpg'
        return self.checkName()
        
    def toPNG(self):
        self.imgExt = '.png'
        return self.checkName()
    
    def toThumb(self, size=(40, 40), filter=Image.ANTIALIAS):
        self.thumb = True
        self.size = size
        self.filter = filter
        return self.checkName()