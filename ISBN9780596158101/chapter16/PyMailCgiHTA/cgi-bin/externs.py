#!/usr/bin/env python3

# Example 16-10
# Encapsulates the location of all external dependencies; if they ever move, 
# this is the only file that must be changed
# Author: Mark Lutz
# Last modified: 

"""
isolate all imports of modules that live outside of the PyMailCgi directory, so 
that their location must only be chnged here if moved; we reuse the mailconfig 
settings that were used for pymailgui2 in ch13; 
PP4E/'s container must be on sys.path to use the last import here;
"""

import sys, os
# sys.path.insert(0, r'C:\Users\mark\Stuff\Books\4E\PP4E\dev\Examples')
sys.path.insert(0, r'..\..\chapter13') 
sys.path.insert(0, r'..\..')                    # relative to script dir

import mailconfig                               # local version
import chapter13 as mailtools                   # mailtools package