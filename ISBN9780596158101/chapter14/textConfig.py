#!/usr/bin/env python3

# Example 14-10
# To customizr display of some pop ups, PyMailGUI relies on PyEdit's own utility, 
# which attempts to load a module like this one from the client application's 
# own directory.
# Author: Mark Lutz
# Last modified: 

"""
customize PyEdit pop-up windows other than the main mail text component;
this module (not its package) is assumed to be on the path for these settings;
PyEdit Unicode settings come from iuts own package's textConfig.py, not this;
"""

bg = 'beige'                # absent=white; colorname or RGB hexstr
fg = 'black'                # absent=black; e.g., 'beige', '#690f96'

# etc -- see PP4E\Gui\TextEditor\textConfig.py
# font = ('courier', 9, 'normal')
# height = 20               # Tk default: 24 lines
# width = 80                # Tk default: 80 characters