#!/usr/bin/env python3

# Example 20-3
# Imports and uses the C extension module
# Author: Mark Lutz, Paul I Ighofose
# Last modified: 2019-04-23

"import and use a C extension library module"

import sys
sys.path.append('../sourceFiles/libraries')
import ch20_hello

print(ch20_hello.message('C'))
print(ch20_hello.message('module ' + ch20_hello.__file__))

for i in range(3):
    reply = ch20_hello.message(str(i))
    print(reply)