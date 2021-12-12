#!/usr/bin/env python3

# Example 5-16
# Uses os._exit to exit from within a processing function, but exits without 
# flushing output stream buffers or running cleaning cleaup handlers
# Author: Mark Lutz
# Last modified: 

def outahere():
    import os
    print('Bye os world')
    os._exit(99)
    print('Never reached')
    
if __name__ == '__main__': outahere()