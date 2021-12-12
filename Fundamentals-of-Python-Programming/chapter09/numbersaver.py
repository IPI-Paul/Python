# Listing 9.7
# Allows the user to enter numbers from the keyboard and save them to a file. It
# also allows the user to retrieve the values previously saved to the file. The 
# user can specify the name of the file and, thus, work woth multiple files.
# Author: Rick Halterman
# Last modified: 

"""
Uses Python's file class to store data and retrieve data from a text file
"""
def load_data(filename):
    """
    Print the elements stored in the text file name filename.
    """
    # Open file to read
    with open(filename) as f:    # f becomes a file object
        for line in f:          # Read each line as text
            print(int(line))    # Convert to an integer and append to the list

def store_data(filename):
    """
    Allows the user to store data to the text file named filename.
    """
    with open(filename, 'w') as f:  # f becomes a file object
        number = 0
        while number != 999:        # Loop until user provides magic number
            number = int(input('Please enter number (999 quits): '))
            if number != 999:
                f.write(str(number) + '\n') # Convert integer to string to save
            else:
                break                       # Exit loop

def main():
    """
    Interactive function that allows the user to create or consume files of 
    numbers.
    """
    done = False
    while not done:
        cmd = input('S)ave L)oad Q)uit: ').upper()
        msg = 'Enter File name: '
        if cmd == 'S':
            store_data(input(msg))
        elif cmd == 'L':
            load_data(input(msg))
        elif cmd == 'Q':
            done = True
            
if __name__ == '__main__':
    main()