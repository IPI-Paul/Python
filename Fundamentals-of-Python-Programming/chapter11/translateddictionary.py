# Listing 11.9
# Uses a dictionary to assist in the translation of some Spanish words into English
# Author: Rick Halterman
# Last modified: 

translator = {'uno': 'one',
              'dos': 'two',
              'tres': 'three',
              'cuatro': 'four',
              'cinco': 'five',
              'seis': 'six',
              'siete': 'seven',
              'ocho': 'eight'}
word = '*'
while word != '':       # Loop until the user presses return by itself
    # Obtain word from user
    word = input('Enter Spanish word: ').lower()
    if word in translator:
        print(translator[word])
    else:
        print('???')    # Unknown word