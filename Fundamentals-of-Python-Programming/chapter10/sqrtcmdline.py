# Listing 10.27
# The user supplies a range of integers on the commandline. The program then 
# prints all the integers in that range along with their square roots.
# Author: Rick Halterman
# Last modified: 

from sys import argv
from math import sqrt

if len(argv) < 3:
    print('Supply range of values')
else:
    x = int(argv[1]) if int(argv[1]) < int(argv[2]) else int(argv[2])
    y = int(argv[1]) if int(argv[1]) > int(argv[2]) else int(argv[2])
    for n in range(x, y + 1):
        print(n, sqrt(n))
    print()