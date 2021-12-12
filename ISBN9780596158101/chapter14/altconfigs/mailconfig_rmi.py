#!/usr/bin/env python3

# Example 14-15
# Allows using alternative accounts without changing mailconfig settings for each
# Author: Mark Lutz
# Last modified: 

from mailconfig_book import *           # get base in . (copied from ..)
popservername = 'pop.rmi.net'           # this is a big inbox: 4800 emails!
popusername = 'lutz'
myaddress = 'lutz@rmi.net'
listbg = 'navy'
listfg = 'white'
listHeight = 20                         # higher initially
viewbg = '#dbbedc'
viewfg = 'black'
wrapsz = 80                             # wrap at 80 cols
fetchlimit = 300                        # load more headers