#!/usr/bin/env python3

# Example 11-2
# Gives the .pyw launching file used to suppress a DOS pop up on Windows when run
# in some modes (for instance, when double-clicked), but still show allow for a 
# console when the .py file is run directly
# Author: Mark Lutz
# Last modified: 

"""
run without a DOS pop up on Windows; could use just a .pyw for both imports and 
launch, but .py file retained for seeing any printed text
"""

exec(open('textEditor.py').read())  # as if pasted here (or textEditor.main())