#!/usr/bin/env python3

# Example 12-16
# Uses the -u flag and makes the spawned script's printed output ape every 2 
# seconds as it is produced
# Author: Mark Lutz
# Last modified: 

# no output for 10 seconds unless Python -u flag used or sys.sdout.flush()
# but writer's output appears here every 2 seconds when either option is used

import os
for line in os.popen('python -u pipe-unbuff-writer.py'):    #iterator reads lines
    print(line, end='')