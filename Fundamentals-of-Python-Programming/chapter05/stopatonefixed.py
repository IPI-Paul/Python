# Listing 5.7
# Uses <= to overcome problems caused by using floating-point numbers in a while
# loop
# Author: Rick Halterman
# Last modified: 

x = 0.0
while x <= 1.0:
    print(x)
    x += 0.1
print("Done")