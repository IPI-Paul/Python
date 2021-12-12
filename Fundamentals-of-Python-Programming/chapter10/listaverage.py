# Listing 10.11
# Uses a list and loop to achieve the generator of Listing 10.2 with the 
# ability to retain all input for later redisplay
# Author: Rick Halterman
# Last modified: 

def main():
    # Set up variables
    sum = 0.0
    NUMBER_OF_ENTRIES = 5
    numbers = []
    
    # Get input from user
    print('Please enter', NUMBER_OF_ENTRIES, 'numbers: ')
    for i in range(0, NUMBER_OF_ENTRIES):
        num = float(input('Enter number ' + str(i) + ': '))
        numbers += [num]
        sum += num
    
    # Print the numbers entered
    print(end = 'Numbers entered: ')
    for num in numbers:
        print(num, end=' ')
    print()
    
    # Print average
    print('Average:', sum / NUMBER_OF_ENTRIES)
    
main()