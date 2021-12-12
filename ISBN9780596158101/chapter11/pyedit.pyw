#!/usr/bin/env python3

# Example 11-3
# Launches PyEdit in a more general and automated fashion. The script disables 
# the DOS pop up when clicked or run via a desktop shortcut on Windows, but also 
# takes care to configure the module search path
# Author: Mark Lutz
# Last modified: 

"""
convenience script to launch pyedit from arbitrary places with the import path 
set as required; sys.path for imports and open() must be relative to the known 
top-level script's dir, not cwd -- cwd is script's dir if run by shortcut or icon
click, but may be anything if run from command-line tyed into a shell console 
window: use argv path; this is a .pyw to suppress console pop-up on Windows; add 
this script's dir to your system PATH to run from command-lines; works on Unix 
too: / and \ handled portably
"""

import sys, os
mydir = os.path.dirname(sys.argv[0])                # use my dir for open, path
sys.path.insert(1, os.sep.join([mydir] + ['..']*3)) # imports PP4E root, 3 up
exec(open(os.path.join(mydir, 'textEditor.py')).read())