#!/usr/bin/env python3

# Example 10-26
# Captures the output of a spawned Python program and displays it in a separately 
# running GUI program's window
# Author: Mark Lutz
# Last modified: 

# GUI reader side: route spawned program standard output to a GUI window

from guiStreams import redirectedGuiShellCmd        # uses GuiOutput
redirectedGuiShellCmd('python -u pipe-nongui.py')   # -u: unbuffered
