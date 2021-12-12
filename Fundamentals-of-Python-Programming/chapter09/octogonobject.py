# Listing 9.12
# Is an enhanced version of Listing 6.19. It organizes the coded into functions 
# for greater modularity and the potential for reuse
# Author: Rick Halterman
# Last modified: 

""" Draws in the window a spiral surrounded with an octogon """

from turtle import *

def octogon(t, x, y, color):
    """
    Draws with turtle t an octogon centered at (x, y)
    """
    t.pencolor(color)          # Set pen color
    t.penup()                  # Lift pen to move it
    t.setposition(x, y)        # Move the pen to coordinates (-45, 100)
    t.pendown()                # Place pen to begin drawing
    for i in range(8):         # Draw eight sides
        t.forward(80)          # Each side is 80 units long
        t.right(45)            # Each vertex is 45 degrees

def spiral(t, x, y, color):
    """ 
    Draws with turtle t a spiral centered at (x, y) with the specified color
    """
    distance = 0.2
    angle = 40
    t.pencolor(color)          # Set pen color
    t.penup()                  # Lift pen to move it
    t.setposition(x, y)        # Position the pen at coordinates (0, 0)
    t.pendown()                # Set pen down to begin drawing
    for i in range(100):
        t.forward(distance)
        t.left(angle)
        distance += 0.5

t = Turtle()                    # Create a turtle objectr named t
octogon(t, -45, 100, 'red')
spiral(t, 0, 0, 'blue')
t.hideturtle()                  # Make t's pen invisible
done()