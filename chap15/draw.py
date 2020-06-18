# Exercise 15.2

import turtle, math

# My other python modules from this chapter
import point, circle

def draw_rect(t, rect):
    """Draw a rectangle with a given turtle object
    t: Turtle object
    rect: Rectangle object
    """
    # turtle.goto(x,y) can be used to move the turtle to the corner
    t.pu() # pen up, don't draw on the way to the corner
    t.goto(rect.corner.x, rect.corner.y)
    t.pd() # pen down
    # turtle.seth(to_angle) faces the turtle in to_angle direction.
    t.seth(90) # Face directly upward
    # Draw vertical line, then horizontal, repeat.
    for i in range(2):
        t.fd(rect.height)
        t.rt(90)
        t.fd(rect.width)
        t.rt(90)

# Draw circle is similar to the circle function in chapter 4

# Start with polygon
def draw_polygon(t, side, n):
    """Draw a regular n-gon with side length side
    t: Turtle
    side: side length
    n: number of sides
    """
    angle = 360/n
    for i in range(n):
        t.fd(side)
        t.rt(angle)
    
    
def draw_circle(t, circ):
    """Draw a circle with a given turtle object
    t: Turtle object
    circ: Circle object
    """
    # The turtle.goto(x,y) method will put the turtle at the center
    # of the circle
    t.pu()
    t.goto(circ.center.x, circ.center.y)
    # Move to edge of circle
    t.fd(circ.radius)
    t.pd()
    t.rt(90) # angle tangent to circle
    # Compute the number of sides of our polygon to draw about 3 pixels/side
    num_sides = int(2*math.pi*circ.radius/3) # must be an integer
    side_length = 3
    draw_polygon(t, side_length, num_sides)
    
# Test drawing functions
def test():
    bob = turtle.Turtle()
    # Draw the same rectangles and circle used in testing circle.py
    spot = point.Point()
    my_circle = circle.Circle()
    spot.x = 150
    spot.y = 100
    my_circle.center = spot
    my_circle.radius = 75
    r1 = point.Rectangle()
    r2 = point.Rectangle()
    p1 = point.Point()
    p1.x = 0
    p1.y = 0
    r1.corner = p1
    r1.width = 140
    r1.height = 90
    p2 = point.Point()
    p2.x = 120
    p2.y = 70
    r2.corner = p2
    r2.width = 60
    r2.height = 60
    draw_rect(bob, r1)
    draw_rect(bob, r2)
    draw_circle(bob, my_circle)
    turtle.mainloop()

if __name__=='__main__':
    test()
