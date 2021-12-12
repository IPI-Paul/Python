#!/usr/bin/env python3

# Example 16-11
# Customizes as desired the local version of Chapter 13's mailconfig 
# Author: Mark Lutz
# Last modified: 

"""
user configuration settings for various email programs (PyMailCGI version);
email scripts get their server names and other email config options from
this module: change me to reflect your machine names, sig, and preferences;
"""

import sys, os

from chapter13.mailconfig import *      # reuse ch13 configs
fetchlimit = 50     # 4E: maximum number headers/emails to fetch on loads (dflt=25)