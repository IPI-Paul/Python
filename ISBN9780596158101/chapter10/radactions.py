#!/usr/bin/env python3

# Example 10-15
# Contains the actual callback handler code. Its functions receive a self 
# argument that gives access back to the Hello class object, as though these
# were real methods
# Author: Mark Lutz
# Last modified: 

# callback handlers: reloaded each time triggered

def message1():                                 # change me
    print('spamSpamSPAM')                       # or could build a dialog...

def message2(self):
    print('Ni! Ni!')                            # change me
    self.method1()                              # access the 'Hello' instance...