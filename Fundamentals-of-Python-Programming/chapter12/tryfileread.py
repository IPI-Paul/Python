# Listing 12.20
# Rectifies the problem with Listing 12.19 by adding exception handling with 
# nested try nested
# Author: Rick Halterman
# Last modified: 

# Sum the values in a text file containing integer values
try:
    f = open('mydata.dat')
except OSError:
    print('Could not open file')
else:
    sum = 0
    try:
        for line in f:
            sum += int(line)
        f.close()   # Close the file
    except Exception as er:
        print(er)   # Show the problem
        f.close()   # Close the file if exception
    print('sum =', sum)