# Listing 11.10
# Reads the content of a text file containing words. After reading the file the 
# program prints a count of each word.
# Author: Rick Halterman
# Last modified: 

"""
Uses a dictionary to count the number of occurences of each word in a text file.
"""

import sys  # For sys.argv global command line arguments list

filename = ''

def main():
    """
    Counts the words in a text file.
    """
    if len(sys.argv) < 2:   # Did the user not supply a filename?
        filename = input('Please give filename: ')
    else:       # User provided file name
        filename = sys.argv[1]
    if filename == '':
        print('Usage: python wordcount.py <filename>')
        print('       where <filename> is the name of the text file.')
    else:       # User provided file name
        counters = {}       # Initialise counting dictionary
        with open(filename, 'r') as f:  # Open the file for reading
            content = f.read()  # Read in content of the entire file
            words = content.split() # Make list of individual words
            for word in words:
                word = word.upper() # Make the word all caps
                if word not in counters:
                    counters[word] = 1  # First occurrence, add the counter
                else:
                    counters[word] += 1 # Increment existing counter
            # Report the counts for each word
            for word, count in counters.items():
                print(word, count)

if __name__ == '__main__':
    main()