#!/usr/bin/env python3

# Example 11-13
# Shows the module that is actually run from the PyDemos launcher script--it 
# predefines a handful of clock styles and runs seven of them at once, attached 
# to new top-level windows for a demo effect
# Author: Mark Lutz
# Last modified: 

# precoded clock configuration styles

from clock import *
from tkinter import mainloop

gifdir = '../sourceFiles/images/'
if __name__ == '__main__':
    from sys import argv
    if len(argv) > 1:
        gifdir = argv[1] + '/'
    
    class PPClockBig(PhotoClockConfig):
        picture, bg, fg = gifdir + 'face.gif', 'navy', 'green'
    
    class PPClockSmall(ClockConfig):
        size = 175
        picture = gifdir + 'face.gif'
        bg, fg, hh, mh = 'white', 'red', 'blue', 'orange'
    
    class GilliganClock(ClockConfig):
        size = 550
        picture = gifdir + 'queen-of-hearts.jpg'
        bg, fg, hh, mh = 'black', 'white', 'green', 'yellow'
    
    class LP4EClock(GilliganClock):
        size =700
        picture = gifdir + 'face.gif'
        bg = 'navy'
    
    class LP4EClockSmall(LP4EClock):
        size, fg = 350, 'orange'
    
    class Pyref4EClock(ClockConfig):
        size, picture = 400, gifdir + 'face.gif'
        bg, fg, hh = 'black', 'gold', 'brown'
    
    class GreyClock(ClockConfig):
        bg, fg, hh, mh, sh = 'grey', 'black', 'black', 'black', 'white'
    
    class PinkClock(ClockConfig):
        bg, fg, hh, mh, sh, = 'pink', 'yellow', 'purple', 'orange', 'yellow'
    
    class PythonPoweredClock(ClockConfig):
        bg, size, picture = 'white', 175, gifdir + 'py-blue-trans-out.jpg'
    
    if __name__ == '__main__':
        root = Tk()
        for configClass in [
            ClockConfig,
            PPClockBig,
            # PPClockSmall,
            LP4EClockSmall,
            GilliganClock,
            Pyref4EClock,
            GreyClock,
            PinkClock,
            PythonPoweredClock
            ]:
            ClockPopup(configClass, configClass.__name__)
        Button(root, text='Quit Clocks', command=root.quit).pack()
        root.mainloop()