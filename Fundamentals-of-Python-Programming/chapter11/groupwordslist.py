# Listing 11.13
# Is a close transliteration of Listing 11.12 that uses a list in place of a 
# dictionary
# Author: Rick Halterman
# Last modified: 

"""
Uses a list to group the words in a text file according to their length 
(number of letters).
"""

import sys      # For argv global command line arguments list

def main():
    """
    Group the words by length in a text file.
    """
    if len(sys.argv) < 2:   # Did the user not supply a file name?
        filename = input('Please give filename: ')
    else:       # User provided file name
        filename = sys.argv[1]
    if filename == '':
        print('Usage: python groupwordslist.py <filename>')
        print('       where <filename> is the name of the text file.')
    else:       # User provided file name
        groups = []       # Initialise grouping list
        for i in range(35):
            groups.append(set())    # Add new empty set to the list
        with open(filename, 'r') as f:  # Open the file for reading
            content = f.read()  # Read in content of the entire file
            words = content.split() # Make list of individual words
            for word in words:
                word = word.upper() # Make the word all caps
                # Compute the word's length
                size = len(word)
                groups[size].add(word)
            # Show the groups
            for size, group in enumerate(groups):
                print(size, ':',  group)

if __name__ == '__main__':
    main()