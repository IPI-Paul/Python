# Listing 9.4
# Uses the len function and [] index operator to print the individual characters
# that make up a string
# Author: Rick Halterman
# Last modified: 

s = 'ABCDEFGHIJK'
print(s)
for i in range(len(s)):
    print('[', s[i], ']', sep='', end='')
print()     # Print newline

for ch in s:
    print('<', ch, '>', sep='', end='')
print() # Print newline