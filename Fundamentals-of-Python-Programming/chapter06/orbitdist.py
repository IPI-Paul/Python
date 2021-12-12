# Listing 6.3
# Uses the math library sqrt, cos, sin, pi and radians to calculate the orbital  
# distance of a satelite
# original code
# Author: Rick Halterman
# Last modified: 

# Use some functions and values from the math module
from math import sqrt, sin, cos, pi, radians

# Get coordinates of the stationary spacecraft, (px, py)
px = float(input('Entrer x coordinate of spacecraft: '))
py = float(input('Enter y coordinate of spacecraft: '))

# Get starting coordinates of satelite, (x1, y1)
x = float(input('Enter initial satelite x coordinate: '))
y = float(input('Enter initial satelite y coordinate: '))

# Convert 60 degrees to radians  to be able to use the trigonometric functions
rads = radians(60)

# Precompute the cosine and sine of the angle
COS_theta = cos(rads)
SIN_theta = sin(rads)

# Make a complete revolution (60 * 60 = 360 degrees)
for increment in range(0, 7):
    # Compute the distance to the satelite
    dist = sqrt((px - x) * (px - x) + (py - y) * (py - y))
    print('Distance to satelite {0:10.2f} km'.format(dist))
    # Compute the satelite's new (x, y) location after rotating by 60 degrees
    x, y = x * COS_theta - y * SIN_theta, x * SIN_theta + y * COS_theta