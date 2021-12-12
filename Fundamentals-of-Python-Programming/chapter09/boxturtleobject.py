# Listing 9.11
# Is the object version of Listing 6.18, which draws a rectangular box within a 
# graphical window
# Author: Rick Halterman
# Last modified: 

# Draws a rectangular box in the window

from turtle import Turtle, mainloop

t = Turtle()        # Create a turtle object named t
t.pencolor('red')  # Set t's pen color to red
t.forward(200)     # Move t's pen forward 200 units (create bottom of rectangle)
t.left(90)         # Turn t's pen by 90 degrees
t.pencolor('blue') # Change t's pen color to blue
t.forward(150)     # Move t's pen forward 150 units (create right wall)
t.left(90)         # Turn t's pen by 90 degrees
t.pencolor('green')# Change t's pen color to green
t.forward(200)     # Move t's pen forward 200 units (create top)
t.left(90)         # Turn t's pen by 90 degrees
t.pencolor('black')# Change t's pen color to black
t.forward(150)     # Move t's pen forward 150 units (create left wall)
t.hideturtle()     # Make t's pen invisible
mainloop()         # Await user input