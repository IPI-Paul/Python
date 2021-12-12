# Listing 12.15
# Illustrates the ability to write a custom version of the int function that 
# behaves similar to the buitl-in int function.
# Author: Rick Halterman
# Last modified: 

def non_neg_int(n):
    result = int(n)
    if result < 0:
        raise ValueError(result)
    return result

while True:
    try:
        x = non_neg_int(input('Please enter a nonnegative integer:'))
        if x == 999:    # Secret number exits loop
            break
        print('You etered', x)
    except ValueError:
        print('The value you entered is not acceptable')