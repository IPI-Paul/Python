#!/usr/bin/env python3

# Example 20-10
# Make the functions of a C extension module accessible by dictionary indexing 
# an integrates with the os.environ object-it guarantees that the object will 
# stay in sync with fetches and changes made by calling the C extension functions
# Author: Mark Lutz
# Last modified: 

import os, sys
sys.path.append('../sourceFiles/libraries')
from ch20_cenviron import getenv, putenv            # get C module's methods

class EnvMapping:                                   # wrap in a Python class
    def __setitem__(self, key, value):
        os.environ[key] = value                     # on writes: Env[key]=value
        putenv(key, value)                          # put in os.environ too
    
    def __getitem__(self, key):
        value = getenv(key)                         # on reads: Env[key]
        os.environ[key] = value                     # integrity check
        return value

Env = EnvMapping()