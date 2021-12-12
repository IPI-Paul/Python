# Listing 7.23
# Refactors the duplicated code in Listing 6.21 into one function that accepts a
# color and y value as a parameter
# Author: Rick Halterman
# Last modified: 

import turtle

def draw_lines(color, y):
    """ Draws 10 horizontal lines of a given color stacked on top of each other 
    with the lowest line appearing at position y on the y axis. """
    turtle.color(color)
    for x in range(10):
        turtle.penup()
        turtle.setposition(-200, y)
        turtle.pendown()
        turtle.forward(400)
        y += 10
        
# Turn off animation
turtle.tracer(0)
draw_lines("red", -200)
draw_lines("blue", -100)
draw_lines("green", 0)
draw_lines("black", 100)

turtle.update()     # Ensure all of image is drawn
turtle.done()