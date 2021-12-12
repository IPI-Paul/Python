#!/usr/bin/env python3

# Example 14-14
# Allows using alternative accounts without changing mailconfig settings for each
# Author: Mark Lutz
# Last modified: 

above = open('../mailconfig.py').read()         # copy version above here (hack?)
open('mailconfig_book.py', 'w').write(above)    # used for 'book' and as others' base
acct = input('Account name?')                   # book, rmi, train
exec('from mailconfig_%s import *' % acct)      # . is first on sys.path
