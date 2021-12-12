# Listing 12.21
# Uses a finally block to consolidate code removing duplication.
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
    except Exception as er:
        print(er)   # Show the problem
    finally:
        f.close()   # Close the file
    print('sum =', sum)