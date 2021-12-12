# Listing 2.17
# Shows how the print() sep='' specifier affects printing between parameters 
# Author: Rick Halterman
# Last modified: 

w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='-----')