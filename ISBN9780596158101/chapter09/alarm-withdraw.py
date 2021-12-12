#!/usr/bin/env python3.6

# Example 9-29
# Illustrates the basics of scheduled callbacks using withdraw to completely 
# erase the window and its icon
# Author: Mark Lutz
# Last modified: 

# same, but hide or show entire window on after() timer callbacks

from tkinter import *
import alarm

class Alarm(alarm.Alarm):
    
    def repeater(self):                             # on every N millisecs
        self.bell()                                 # beep now
        if self.master.state() == 'normal':         # is window displayed?
            self.master.withdraw()                  # hide entire window, no icon
        else:                                       # iconify shrinks to an icon
            self.master.deiconify()                # else redraw entire window
            self.master.lift()                      # and raise above others
            self.after(self.msecs, self.repeater)       # reschedule handler
            
if __name__ == '__main__': Alarm().mainloop()       # master = default Tk root