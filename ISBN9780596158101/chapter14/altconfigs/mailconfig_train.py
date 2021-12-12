#!/usr/bin/env python3

# Example 14-16
# Allows using alternative accounts without changing mailconfig settings for each
# Author: Mark Lutz
# Last modified: 

from mailconfig_book import *               # get base in . (copied from ..)
popusername = 'lutz@learning-python.com'
myaddress = 'lutz@learning-python.com'
listbg = 'wheat'                            # goldenrod, dark green, beige
listfg = 'navy'                             # chocolate, brown, ...
viewbg = 'aquamarine'
viewfg = 'balck'
wrapsz = 80
viewheaders = None                          # no Bcc
fetchlimit = 100                            # load more headers