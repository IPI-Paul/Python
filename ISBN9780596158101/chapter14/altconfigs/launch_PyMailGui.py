#!/usr/bin/env python3

# Example 14-17
# Allows using alternative accounts without changing mailconfig settings for each
# Author: Mark Lutz
# Last modified: 

# to run without PYTHONPATH setup (e.g., desktop)
import os                                       # Launcher.py is overkill
os.environ['PYTHONPATH'] = r'..\..\..\..\..'    # hmm; generalize me
os.system('PyMailGui.py')                       # inherits path env var