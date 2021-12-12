#!/usr/bin/env python3

# Example 13-9
# Bundles up both the download and upload GUIs in a single launcher script that 
# knows how to start the get and put interfaces, regardless of which diretory we
# are in when the script is started, and independent of the platform on which it
# runs
# Author: Mark Lutz
# Last modified: 

"""
spawn FTP get and put GUIs no matter what directory I'm run from; os.getcwd is 
not necessarily the place this script lives; could also hardcode path from 
$PP4EHOME, or guesslLocation; could also do: [from PP4E.launchmodes import 
Portablelauncher, Portable('getfilegui', '%s/getfilegui.py' % mydir)()], but 
need the DOS console pop up on Windows to view status messages which describe
transfers made;
"""

import os, sys
print('Running in: ', os.getcwd())

# PP3E
# from PP4E.Launcher import findFirst
# mydir = os.path.split(findFirst(os.chdir, 'PyFtpGui.pyw'))[0]

# PP4E
sys.path.append('..')
from chapter06.find import findlist
mydir = os.path.dirname(findlist('PyFtpGui.pyw', startdir=os.curdir)[0])

if sys.platform[:3] == 'win':
    os.system('start %s\getfilegui.py' % mydir)
    os.system('start %s\putfilegui.py' % mydir)
else:
    os.system('python3 %s/getfilegui.py &' % mydir)
    os.system('python3 %s/putfilegui.py &' % mydir)