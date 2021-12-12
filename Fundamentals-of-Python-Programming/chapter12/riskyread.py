# Listing 12.19
# Opens a file and reads its contents.
# Author: Rick Halterman
# Last modified: 

# Sum the values in a text file containing integer values
sum = 0
f = open('mydata.dat')
for line in f:
    sum += int(line)
f.close()   # Close the file
print(sum)