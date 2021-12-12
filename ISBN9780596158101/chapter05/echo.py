#!/usr/bin/env python3

# Example
# Echos back input
# Author: Mark Lutz
# Last modified: 

try:
    print('Spam')
    input('press Enter')
except EOFError as e:
    pass