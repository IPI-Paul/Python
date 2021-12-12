#!/usr/bin/env python3

# Example 5-15
# Uses sys.exit to exit from within a processing function
# Author: Mark Lutz
# Last modified: 

def later():
    import sys
    print('Bye sys world')
    sys.exit(42)
    print('Never reached')

if __name__ == '__main__': later()