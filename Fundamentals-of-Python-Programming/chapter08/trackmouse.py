# Listing 8.10
# Is a very simple program that shows how onscreenclick works
# Author: Rick Halterman
# Last modified: 

import turtle

def report_position(x, y):
    """ Simply prints thje values of x and y. """
    print ("x =", x, " y =", y, flush = True)

# Establis a function framework should call when the clicks the mouse
turtle.onscreenclick(report_position)

# Start the graphics loop that listens for the user input
turtle.mainloop()