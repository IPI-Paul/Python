#!/usr/bin/env python3

# Example 10-32
# Imports and calls the appropriate function with an imported program list
# Author: Mark Lutz
# Last modified: 

"""
run a PyGadgets toolbar only, instead of starting all the gadgets immediately;
filename avoids DOS pop up on Windows: rename to '.py' to see console messages
"""

import PyGadgets
PyGadgets.runLauncher(PyGadgets.mytools)
