#!/usr/bin/env python3

# Example 13-3
# Encapsulates and simplifies ftplib in to tweo function calls plus a password 
# prompt, but with a net effect exactly like Example 13-1 when run
# Author: Mark Lutz
# Last modified: 

"""
A Python script to download and play a media file by FTP. 
Uses getfile.py, a utility module which encapsultaes FTP step
"""

import getfile, sys, os
from getpass import getpass
filename = 'Earth.jpg'

# fetch with utility
getfile.getfile(file=filename, 
                site='localhost',
                dir='Java/ISBN100134177290/sourceFiles/images',
                # user=('lutz', getpass('Pswd?')),
                user=(input('User Name: '), getpass('Pswd?')),
                refetch=True)

# rest is the same 
if input('Open file?') in ['Y', 'y']:
    sys.path.append('..')    
    from chapter06.playfile import playfile
    playfile(filename)