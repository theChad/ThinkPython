import point

# Exercise 15.1

# Define class circle

class Circle():
    """Circle
    attributes: center, radius
    """

def point_in_circle(circle, p):
    """True if point is in circle
    circle: Circle object
    p: Point object
    """
    # point is in circle if the distance between point and
    # the center of circle is not greater than the radius
    return circle.radius >= point.distance_between_points(circle.center, p)

def get_rect_corners(rect):
    """Return a list of all corners of rect
    rect: Rectangle object
    """
    # Create a list of 4 empty points
    corners = []
    for i in range(4):
        corners.append(Point())
        
    # Find the corners
    corners[0].x = rect.corner.x
    corners[0].y = rect.corner.y
    corners[1].x = rect.corner.x
    corners[1].y = rect.corner.y + rect.height
    corners[2].x = rect.corner.x + rect.width
    corners[2].y = rect.corner.y + rect.height
    corners[3].x = rect.corner.x + rect.width
    corners[3].y = rect.corner.y
    return corners

def rect_in_circle(circle, rect):
    """True if rect is entirely within circle
    circle: Circle object
    rect: Rectangle ojbect
    """
    # rect is in circle if all four corners of rect are in circle
    corners = get_rect_corners(rect)
    for corner in corners:
        if not point_in_circle(circle, corner):
            return False
    return True

def rect_circle_overlap(circle, rect):
    """True if *any* corners of rect are within circle
    circle: Circle object
    rect: Rectangle object
    """
    corners = get_rect_corners(rect)
    for corner in corners:
        if point_in_circle(circle, corner):
            return True
    return False

# Test functions

def test():
    spot = point.Point()
    dot = point.Point()
    plop = point.Point()
    my_circle = Circle()
    spot.x = 150
    spot.y = 100
    my_circle.center = spot
    my_circle.radius = 75
    dot.x = 0
    dot.y = 0
    plop.x = 75
    plop.y = 100
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
    print(dot.x, dot.y, "in circle:", point_in_circle(my_circle, dot))
    print(spot.x, spot.y, "in circle:", point_in_circle(my_circle, spot))
    print(plop.x, plop.y, "in circle:", point_in_circle(my_circle, plop))
    print("R1 in circle: ", rect_in_circle(my_circle, r1))
    print("R1 corners:")
    for corner in get_rect_corners(r1):
        print(corner.x, corner.y)
    print("R1 overlap:", rect_circle_overlap(my_circle, r1))
    print("R2 in circle: ", rect_in_circle(my_circle, r2))
    print("R2 overlap:", rect_circle_overlap(my_circle, r2))

if __name__=='__main__':
    test()
