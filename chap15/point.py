import math, copy

# Point class definition

class Point():
    """Cartesian coordinate point
    """

# Section 15.2 exercise

def distance_between_points(p1, p2):
    """Find the distance between points p1 and p2
    p1, p2: Point objects
    """
    ydiff = p2.y-p1.y
    xdiff = p2.x-p1.x
    distance = math.sqrt(ydiff**2 + xdiff**2)
    return distance

# Section 15.5 exercise

class Rectangle():
    """Rectangle
    attributes: corner, width, height
    """

def move_rectangle(rect, dx, dy):
    """Shift rectangle in space by (dx,dy)
    rect: Rectangle object
    dx, dy: numbers
    """
    rect.corner.x += dx
    rect.corner.y += dy

# Section 15.6 exercise

def move_rectangle_copy(rect, dx, dy):
    """Return a shifted copy of rect
    rect: Rectangle object
    dx, dy: numbers
    """
    # Make a full deep copy of rect
    rect_copy = copy.deepcopy(rect)
    # Now move that copy
    move_rectangle(rect_copy, dx, dy)
    return rect_copy

# Test out exercises

def test_exercise():
    spot = Point()
    spot.x = 1
    spot.y = 2
    dot = Point()
    dot.x = 3
    dot.y = 5
    print("Distance between spot and dot it is", distance_between_points(spot, dot))

    # Rectangle test
    box = Rectangle()
    box.corner = spot
    box.width = 4
    box.height = 10
    # Keep track of the original corner of the box
    old_x = spot.x
    old_y = spot.y
    move_rectangle(box, 3, 4)
    # Note that this *also* changed spot, since it's mutable.
    # box.corner and spot now refer to the same object, so
    # when we change box.corner in move_rectangle, the same thing happens
    # to spot
    print("Moved rectangle from (", old_x, old_y, ") to (", box.corner.x,
          box.corner.y,")")
    


if __name__=='__main__':
    test_exercise()
