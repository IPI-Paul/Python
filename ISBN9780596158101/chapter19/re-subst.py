#!/usr/bin/env python3

# Example 19-4
# A short test file that matches simple but representative pattern forms. re also 
# includes tools for substring replacement or substitution
# Author: Mark Lutz
# Last modified: 

"substitutions: replace occurences of pattern in string"

import re
print(re.sub('[ABC]', '*', 'XAXAXBXBXCXC'))
print(re.sub('[ABC]_', '*', 'XA-XA_XB-XB_XC-XC_'))      # alternatives char + _

print(re.sub('(.) spam', 'spam\\1', 'x spam, y spam'))  # group back ref (or r'')

def mapper(matchobj):
    return 'spam' + matchobj.group(1)

print(re.sub('(.) spam', mapper, 'x spam, y spam'))     # mapping function