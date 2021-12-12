#!/usr/bin/env python3

# Example 11-9
# Shows a MovingPics subclass that codes the necessary customizations to do 
# parallel moves with after events. It allows any number of objects in the canvas,
# including pictures, to be moving independently at once
# Author: Mark Lutz
# Last modified: 

"""
PyDraw-after: simple canvas paint program and object mover/animator use 
widget.after scheduled events to imp[lement object move loops, such that more 
than one can be in motion at once without having to use threads; this does moves 
in parallel, but seems to be slower than time.sleep version; see also canvasDraw 
in Tour: builds and passes the incX/incY list at once: here, would be 
allmoves = ([(incrX, 0)] * reptX) + ([(0, incrY)] * reptY)
"""

from movingpics import *

class MovingPicsAfter(MovingPics):
    def doMoves(self, delay, objectId, incrX, reptX, incrY, reptY):
        if reptX:
            self.canvas.move(objectId, incrX, 0)
            reptX -= 1
        else:
            self.canvas.move(objectId, 0, incrY)
            reptY -= 1
        if not (reptX or reptY):
            self.moving.remove(objectId)
        else:
            self.canvas.after(delay,
                              self.doMoves, delay, objectId, incrX, reptX, 
                              incrY, reptY)
    def onMove(self, event):
        traceEvent('onMove', event, 0)
        object = self.object                # move cur obj to click spot
        if object:
            msecs = int(pickDelays[0] * 1000)
            parms = 'Delay=%d msec, Units=%d' %(msecs, pickUnits[0])
            self.setTextInfo(parms)
            self.moving.append(object)
            incrX, reptX, incrY, reptY = self.plotMoves(event)
            self.doMoves(msecs, object, incrX, reptX, incrY, reptY)
            self.where = event

if __name__ == '__main__':
    from sys import argv                    # when this file is executed
    if len(argv) == 2:
        import movingpics                   # not tjhis module's global
        movingpics.PicDir = argv[1]         # and from* doesn't link names
    root = Tk()
    MovingPicsAfter(root)
    root.mainloop()