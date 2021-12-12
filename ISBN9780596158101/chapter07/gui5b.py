#!/usr/bin/env python3

# Example 7-19
# Uses OOP to standardise behaviour and Specifies callback handlers by overiding 
# the callback method in subclasses
# Author: Mark Lutz
# Last modified: 

from gui5 import HelloButton

class MyButton(HelloButton):                    # subclass HelloButton
    
    def callback(self):                         #redefine press-handler method
        print('Ignoring press!...')

if __name__ == '__main__':
    MyButton(None, text='Hello subclass world').mainloop()