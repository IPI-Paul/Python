# Listing 6.21
# Demonstrates the subtle difference in the way speed and delay functions effect
# the time to render an image, but with using the tracer function the picture
# appears almost instantly
# Author: Rick Halterman
# Last modified: 

import turtle

y = -200    # Initial y value

# Turn off animation
turtle.tracer(0)
turtle.color('red')
for x in range(10):
    turtle.penup()
    turtle.setposition(-200, y)
    turtle.pendown()
    turtle.forward(400)
    y += 10
    
turtle.color('blue')
for x in range(10):
    turtle.penup()
    turtle.setposition(-200, y)
    turtle.pendown()
    turtle.forward(400)
    y += 10
    
turtle.color('green')
for x in range(10):
    turtle.penup()
    turtle.setposition(-200, y)
    turtle.pendown()
    turtle.forward(400)
    y += 10

turtle.color('black')
for x in range(10):
    turtle.penup()
    turtle.setposition(-200, y)
    turtle.pendown()
    turtle.forward(400)
    y += 10

turtle.done()