# Listing 9.6
# Opens a file named data.dat for reading and reads in and prints out each line.
# It uses the with/as statement to create what is known as a context manager 
# that ensures the file is closed after its use
# Author: Rick Halterman
# Last modified: 

with open('data.dat') as f:     # f becomes a file object
    for line in f:              # Read each line as text
        print(line.strip())     # Remove tailing newline character
    # No need to close file