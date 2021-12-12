# Listing 11.7
# Uses a Python dictionary to implement a simple telephone contact database with
# a rudimentary command line interface.
# Author: Rick Halterman
# Last modified: 

contacts = {}       # the global telephone contact list

running = True

while running:
    command = input('A)dd  D)elete  L)ook up  Q)uit: ').upper()
    if command == 'A': 
        name = input('Enter new name: ')
        print('Enter phone number for ', name, end=':')
        number = input()
        contacts[name] = number
    elif command == 'D':
        name = input('Enter name to delete: ')
        del contacts[name]
    elif command == 'L':
        name = input('Enter name: ')
        print(name, contacts[name])
    elif command == 'Q':
        running = False
    elif command == 'DUMP':  # Secret command
        print(contacts)
    else:
        print(command, 'is not a valid command')