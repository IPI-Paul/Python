# Listing 7.7
# Uses a custom function to compute the midpoint between two mathematical points
# Author: Rick Halterman
# Last modified: 

def midpoint(pt1, pt2):
    x1, y1 = pt1    # Extract x and y components from the first point
    x2, y2 = pt2    # Extract x and y components from the second point
    return (x1 + x2) / 2, (y1 + y2) / 2

# Get two points from the user
point1 = float(input("Enter first point's x: ")), \
    float(input("Enter first point's y: "))
point2 = float(input("Enter second point's x: ")), \
    float(input("Enter second point's y: "))
mid = midpoint(point1, point2)
# Report result to user
print('Midpoint of', point1, 'and', point2, 'is', mid)