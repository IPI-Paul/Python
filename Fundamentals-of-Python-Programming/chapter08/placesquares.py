# Listing 8.11
# Draws a square centered at each location the user clicks the mouse
# Author: Rick Halterman
# Last modified: 

import turtle

def draw_square(x, y):
    """ Draws a 10 x 10 square centered at point (x, y). """
    turtle.penup()
    turtle.setheading(0)    # Ensure the pen is pointed the proper direction
    turtle.setposition(x - 5, y - 5)    # Ceter the square
    turtle.pendown()
    for i in range(4):
        turtle.forward(10)
        turtle.left(90)
    turtle.update()

# Turn off animation
turtle.tracer(0)
turtle.hideturtle()

# Allow user to place 10 x 10 squares using mouse
turtle.onscreenclick(draw_square)

# Start the graphics loop that listens for user input
turtle.mainloop()