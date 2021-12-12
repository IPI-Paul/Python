#!/usr/bin/env python3

# Example 10-27
# Writes a standard output, and is not concerned with creating a socket interface
# Author: Mark Lutz
# Last modified: 

# non-GUI side: proceed normally, no need for special code

import time
while True:                                 # non-GUI code
    print(time.asctime())                   # sends to GUI process
    time.sleep(2.0)                         # no need to flush here