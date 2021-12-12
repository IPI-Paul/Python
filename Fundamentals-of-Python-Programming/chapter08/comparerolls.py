# Listing 8.31
# Pulls everything together into an executable program using the partial 
# function
# Author: Rick Halterman
# Last modified: 

from random import randint
from functools import partial

def read_file(filename, n, val):
    """
    Reads n integers from the text file named filename.
    Returns the number of times vall appears in the file.
    """
    count, read = 0, 0
    with open(filename, 'r') as f:
        for value in f.readlines():
            read += 1
            # Have we read enough lines yet?
            if read > n:
                break
            # Convert text integer into an actual integer
            if int(value) == val:
                count += 1
    return count

def roll(n, val):
    """
    Simulates the roll of a pair of dice n times. 
    Returns the number of times a roll resulted in val.
    """
    count = 0
    for i in range(n):
        roll = randint(1, 6) + randint(1, 6)
        if roll == val:
            count += 1
    return count

def run_trials(f, f1, n):
    """
    Performs n experiments using function f as the source of outcomes.
    Counts the number of occurences of each possible outcome.
    """
    for value in range(2, 13):
        print("{:>3}:{:>5} {:>8}".format(value, f(n, value), f1(n, value)))

# Compare the actual experiments to the simulation
number_of_trials = 100
# print('---Pseudorandom number rolls---')
# run_trials(roll, number_of_trials)
# print('---Actual experimental data---')
# run_trials(partial(read_file, 'dicedata.data'), number_of_trials)
print('      Pseudo   Actual')
run_trials(roll, partial(read_file, 'dicedata.data'), number_of_trials)