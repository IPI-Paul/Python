# Listing 7.16
# Illustrates that some functions are useful even if they accept no information
# and return no result
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
    return float(input("Enter arg " + str(n) + ": "))

def main():
    """ Runs a command loop that allows users to perform simple arithmetic. """
    result = 0.0
    done = False        # initially not done
    while not done:
        choice = menu()     # Get user's choice
        
        if choice == "A" or choice == "a":      # Addition
            arg1 = get_float(1)
            arg2 = get_float(2)
            result = arg1 + arg2
            print(result)
        elif choice == "S" or choice == "s":    # Subtraction
            arg1 = get_float(1)
            arg2 = get_float(2)
            result = arg1 - arg2
            print(result)
        elif choice == "P" or choice == "p":    # Print
            print(result)
        elif choice == "H" or choice == "h":    # Help
            help_screen()
        elif choice == "Q" or choice == "q":    # Quit
            done = True
        
main()