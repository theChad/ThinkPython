import turtle
import math # this is another module that contains things like pi

#bob = turtle.Turtle()

# 4.3.1
# ----------------
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
#square(bob)

# 4.3.2
# ---------------
def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
#square(bob,250)

# 4.3.3
# ---------------
# Draw a polygon of n sides, each side length long
def polygon(t, length, n):
    polygon_angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(polygon_angle)
#polygon(bob, 100, 8)

# 4.3.4
# --------------
# Approximate a circle with a polygon
# It doesn't say to allow number of sides as an input, but I will
# "sides=100" as the last argument means that if I only give 2 arguments,
# it'll default to giving sides a value of 100. 
def circle(t, r, sides=100):
    circle_circumference = 2 * math.pi * r
    side_length = circle_circumference/sides
    polygon(t, side_length, sides)
#circle(bob, 100)

# 4.3.5
# ---------------
# Draw just part of a circle. Note that sides is still the last parameter,
# so we can give it a default value and leave it off if we want.
# I also added a default for angle, so if you leave off the last two arguments
# it'll draw a full 100-sided polygon.
def arc(t, r, angle=360, sides=100):
    arc_length = 2 * math.pi * r * angle / 360
    side_length = arc_length/sides
    polygon_angle = angle/sides # each internal angle of the polygon
    for i in range(sides):
        t.fd(side_length)
        t.lt(polygon_angle) # may as well use the variable name now

#arc(bob, 200, 90)
#arc(bob, 50, sides=10)


