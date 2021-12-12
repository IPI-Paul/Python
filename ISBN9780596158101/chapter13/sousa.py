#!/usr/bin/env python3

# Example 13-6
# Downloads and plays a sample file
# Author: Mark Lutz
# Last modified: 

"""
Usage: sousa.py Fetch and play the Monty Python theme song.
This will not work on your system as is: it requires a machine with Internet 
access, and uses audio filters on Unix and your .au player on Windows. Configure
this and playfile.py as needed for your platform.
"""

from getpass import getpass
from getfile import getfile
import sys, os 
sys.path.append('..')
from chapter06.playfile import playfile

file ='ofthepeople.au'          # default file coordinates
site = 'localhost'              # Monty Python theme song
dir = 'Python/ISBN9780596158101/sourceFiles/audio'
user = (input('User Name: '), getpass('Pswd?'))

getfile(file, site, dir, user)  # fetch audio file by FTP
playfile(file)                  # send it to audio player

# import os
# os.system('getone.py sousa.au')   # equivalent command line