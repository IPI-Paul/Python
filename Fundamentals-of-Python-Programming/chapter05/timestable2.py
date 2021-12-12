# Listing 5.17
# Uses a for loop with a nested for loop to advance a multiplication table
# Author: Rick Halterman
# Last modified: 

# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
for row in range(1, size + 1):
    for column in range(1, size + 1): 
        product = row * column          # Compute product
        print(product, end=' ')         # Display product
    print()                             # Move cursor to next row