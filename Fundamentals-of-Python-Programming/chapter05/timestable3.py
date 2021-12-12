# Listing 5.18
# Uses a for loop with a nested for loop to advance a multiplication table, then
# applies formatting to space the results evenly
# Author: Rick Halterman
# Last modified: 

# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
for row in range(1, size + 1):
    for column in range(1, size + 1): 
        product = row * column                      # Compute product
        print('{0:4}'.format(product), end='')      # Display product
    print()                                         # Move cursor to next row