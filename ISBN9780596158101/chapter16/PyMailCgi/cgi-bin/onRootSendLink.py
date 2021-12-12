#!/usr/bin/env python3

# Example 16-3
# The root page Send function steps users through two other pages: one to edit a 
# message and one to confirm delivery
# Author: Mark Lutz
# Last modified: 

"""
################################################################################
On 'send' click in main root window: display composition page
################################################################################
"""
import commonhtml
from externs import mailconfig

commonhtml.editpage(kind='Write', headers={'From': mailconfig.myaddress})