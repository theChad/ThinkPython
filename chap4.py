import mypolygon # I'll want to use functions from mypolygon.py
import turtle
import math

# 4.1.1
# Stack diagram, from circle(bob, radius) fuction call in
# provided polygon.py

#----------------------------------------------
# __main__     |         bob -> turtle.Turtle()
#              |      radius -> 100
#----------------------------------------------
# circle       |           t -> bob
#              |           r -> 100
#----------------------------------------------
# arc          |           t -> bob
#              |           r -> 100
#              |       angle -> 360
#              |  arc_length -> 628.318
#              |           n -> 160
#              | step_length -> 3.927
#              |  step_angle -> 2.25
#----------------------------------------------
# polyline     |           t -> bob
#              |           n -> 160
#              |      length -> 3.927
#              |       angle -> 2.25
#----------------------------------------------

# 4.2

def petal(t, circle_radius, angle):
    """ Draw a petal using arcs of given circle radius and angle
    """
    petal_point_angle = 180 - angle
    for i in range(2):
        mypolygon.arc(t, circle_radius, angle, 10)
        t.lt(petal_point_angle)

def turtle_flower(t, r, angle, num_petals):
    """ Draws a flower of radius r, using arcs of the appropriate circle
    subtended by angle. t is a turtle.
    """
    # The circle radius is just for scaling, so that the flower has
    # a radius of r. Could leave it out and just use r instead of
    # circle_radius, but then the flower would vary with the angle provided
    # for the arc
    circle_radius = r/(2*math.sin(math.radians(angle/2)))
    petal_point_angle = 180 - angle
    petal_center_angle = 360/num_petals
    #num_petals = int(720/angle)
    for i in range(num_petals):
        petal(t, circle_radius, angle)
        t.lt(petal_center_angle)

# Draw the flowers
def skip_back(t, distance):
    """ Move turtle back without drawing
    """
    t.pu()
    t.bk(distance)
    t.pd()
def skip_forward(t, distance):
    """ Move turtle forward without drawing
    """
    t.pu()
    t.fd(distance)
    t.pd()
    
def draw_3_flowers():
    bob = turtle.Turtle()
    skip_back(bob, 200)
    turtle_flower(bob, 100, 60, 7)
    skip_forward(bob,200)
    turtle_flower(bob, 100, 90, 10)
    skip_forward(bob, 200)
    turtle_flower(bob, 100, 20, 20)
    turtle.mainloop()

#draw_3_flowers()

# 4.3

def draw_slice(t, r, center_angle):
    """ Draw a (straight-line) pie slice
    r: radius of pie, center to vertex
    center_angle: center angle of slice
    """
    # sum of triangle angles is 180. The left turn will actually be the
    # supplement of the angle *inside* the triangle though.
    edge_angle = 180-(180 - center_angle)/2
    # Use trigonometry to find the base of this isosceles triangle,
    # treating it as two right triangles back to back.
    edge_length = 2 * r * math.sin(math.radians(center_angle/2))
    t.fd(r) #draw right side of piece
    t.lt(edge_angle)
    t.fd(edge_length) # draw outside edge of piece
    t.lt(edge_angle)
    t.fd(r) # draw left side of piece
    t.lt(180) #flip back around to face outward again

def draw_pie(t, r, n):
    """ Draw a polygon pie, sliced up
    r: radius of polygon, center to vertex
    n: number of sides
    """
    center_angle = 360/n
    # Pie slices already end facing out, so we can just start the next
    # slice with no further prep.
    for i in range(n):
        draw_slice(t, r, center_angle)

def draw_3_pies():
    bob=turtle.Turtle()
    skip_back(bob, 200)
    draw_pie(bob, 100, 5)
    skip_forward(bob, 200)
    draw_pie(bob, 100, 6)
    skip_forward(bob, 200)
    draw_pie(bob, 100, 7)
    turtle.mainloop()

#draw_3_pies()

# 4.4
# 26 fuctions? One for every letter? Maybe some other time..

# 4.5
