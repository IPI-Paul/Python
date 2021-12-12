# Listing 10.26
# Is a program meant to be exectued from the command line with extra arguments.
# It simply reports the extra information the user supplied.
# Author: Rick Halterman
# Last modified: 

import sys

for arg in sys.argv:
    print('[' + arg + ']')