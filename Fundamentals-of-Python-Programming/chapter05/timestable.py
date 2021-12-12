# Listing 5.16
# Uses a for loop to begin a multiplication table
# Author: Rick Halterman
# Last modified: 

# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
for row in range(1, size + 1):
    print("Row #", row)