# Listing 8.1
# Is a modification of Listing 7.16 that uses global variables named result, 
# arg1, and arg2 which are shared by several functions in the program
# Author: Rick Halterman
# Last modified: 

def help_screen():
    """
    Displays information about how the program works.
    Accepts no parameters.
    Returns nothing.
    """
    print("Add:       Adds two numbers")
    print( "subtract: Subtracts two numbers")
    print("Print:     Displays the result of the latest operation")
    print("Help:      Displays the help screen")
    print("Quit:      Exits the program")
    
def menu():
    """
    Displays a menu
    Accepts no parameters
    Returns the string entered by the user.
    """
    return input("===A)dd S)ubract P)rint H)elp Q)uit ===")

def get_float(n):
    return float(input("Enter argument #" + str(n) + ": "))

# Global variables used by several functions
result = 0.0
arg1 = 0.0
arg2 = 0.0

def get_input():
    """
    Assigns the globals arg1 and arg 2 from user keyboard input
    """
    global arg1, arg2   # arg1 and arg2 are globals
    arg1 = get_float(1)
    arg2 = get_float(2)

def report():
    """ Reports the value of the global result """
    # Not assigning to result, gloabl keyword not needed
    print(result)
    
def add():
    """ 
    Assigns the sum of the globals arg1 and arg2 to the global variable result
    """
    global result   # Assigning to result, global keyword needed
    result = arg1 + arg2

def subtract():
    """ 
    Assigns the difference of the globals arg1 and arg2 to the global variable 
    result
    """
    global result   # Assigning to result, global keyword needed
    result = arg1 - arg2

def main():
    """ Runs a command loop that allows users to perform simple arithmetic. """
    done = False        # initially not done
    while not done:
        choice = menu()     # Get user's choice
        
        if choice == "A" or choice == "a":      # Addition
            get_input()
            add()
            report()
        elif choice == "S" or choice == "s":    # Subtraction
            get_input()
            subtract()
            report()
        elif choice == "P" or choice == "p":    # Print
            report()
        elif choice == "H" or choice == "h":    # Help
            help_screen()
        elif choice == "Q" or choice == "q":    # Quit
            done = True
        
main()