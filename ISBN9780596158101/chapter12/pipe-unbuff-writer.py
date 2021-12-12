#!/usr/bin/env python3

# Example 12-15
# Is non-socket and does not fully buffer its output when it is connected to a
# terminal (output is on line buffered when run from a shell command prompt),
# but does if connected to something else (including a socket or pipe)
# Author: Mark Lutz
# Last modified: 

# output line buffered (unbuffered) if stdout is a terminal, buffered by default for
# other devices: use -u or sys.stdout.flush() to avoid delayed output on pipe/socket

import time, sys
for i in range(5):
    print(time.asctime())           # print transfers per stream buffering
    sys.stdout.write('spam\n')      # ditto for direct stream file access
    time.sleep(2)                   # unless sys.stdout reset to other file