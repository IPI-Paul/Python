# Listing 11.11
# Provides the complete code using a list comprehension expression to strip out
# newline characters and strip final commas along with trailing spaces. It also 
# splits the data using commas
# Author: Rick Halterman
# Last modified: 

def readfile(filename): 
    """
    Read the comma-separated integer data from the text file name filename and 
    return the data in a list.
    """
    result = []        # List initially empty
    with open(filename, 'r') as f:
        for line in f:
            # Remove any trailing spaces, comma, and newline
            result += [int(x.strip()) for x in line.rstrip(' ,\n').split(',')]
    return result

def main():
    lst = readfile('monitor.data')
    print(lst)
    
if __name__ == '__main__':
    main()