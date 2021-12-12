#!/usr/bin/env python3

# Example 1-16
# Customises the Person class in order to give a 10 percent bonus by default to 
# managers whenever the receive a raise
# Author: Mark Lutz
# Last modified: 

from person import Person

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
