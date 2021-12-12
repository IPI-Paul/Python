# Listing 5.6
# Demonstrates problems caused by using floating-point numbers in a while loop
# Author: Rick Halterman
# Last modified: 

x = 0.0
while x != 1.0:
    print(x)
    x += 0.1
    if x > 1.2:
        print("Failed to terminate")
        x = 1.0
print("Done")