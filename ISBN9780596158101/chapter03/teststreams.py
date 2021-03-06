#!/usr/bin/env python3

# Example 3-5
# Is a simple read-evaluate-print loop program
# Author: Mark Lutz
# Last modified: 

'read numbers till eof and show squares'

def interact():
    print('Hello stream world')                 # print sends to sys.stdout
    while True:
        try:
            reply = input('Enter a number>')    # input reads sys.stdin
        except EOFError:
            break                               # raises and except eof
        else:                                   # input given as a string
            num = int(reply)
            print('%d squared is %d' % (num, num ** 2))
    print('Bye')

if __name__ == '__main__':
    interact()                                  # when run, not imported