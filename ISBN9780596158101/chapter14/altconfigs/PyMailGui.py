#!/usr/bin/env python3

# Example 14-13
# Allows using alternative accounts without changing mailconfig settings for each
# Author: Mark Lutz
# Last modified: 

import sys                              # ..\PyMailGui.py or 'book' for book configs
sys.path.insert(1, '..')                # add visibility for real dir
exec(open('../PyMailGui.py').read())    # do this, but get mailconfig here
