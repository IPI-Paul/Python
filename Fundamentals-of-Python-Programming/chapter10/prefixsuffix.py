# Listing 10.20
# Prints all the prefixes and suffixes of the list [1, 2, 3, 4, 5, 6, 7, 8]
# Author: Rick Halterman
# Last modified: 

a = [1, 2, 3, 4, 5, 6, 7, 8]
print('Prefixes of', a)
for i in range(0, len(a) + 1):
    print('<', a[0:i], sep='')
print('-----------------------------')
print('Suffixes of', a)
for i in range(0, len(a) + 1):
    print('<', a[i:len(a) + 1], '>', sep='')