# Listing 9.3
# Demonstrates the strip and count string methods
# character
# Author: Rick Halterman
# Last modified: 

# Strip leading and trailing whitespace and count substrings
s = "          ABCDEFGHBCDIJKLMNOPQRSBCDTUVWXYZ            "
print('[', s, ']', sep='')
s = s.strip()
print('[', s, ']', sep='')

# Count occurerences of the substring 'BCD'
print(s.count('BCD'))