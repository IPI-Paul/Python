# Listing 9.5
# Opens a file named data.dat for reading and reads in and prints out each line 
# of text
# Author: Rick Halterman
# Last modified: 

f = open('data.dat')            # f becomes a file object
for line in f:                  # Read each line as text
    print(line.strip())         # Remove trailing newline character
f.close()