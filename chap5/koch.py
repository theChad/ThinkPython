# Exercise 5.6
import turtle

# 5.6.1
def koch(t, x):
    """Draw a koch curve.
    t: Turtle object
    x: length parameter of koch curve
    """
    if x < 3:
        t.fd(x)
    else:
        # Just follow the directions in the exercise as if we already had
        # a koch function that did what we wanted. Recursion takes care of the rest.
        koch(t, x/3)
        t.lt(60)
        koch(t, x/3)
        t.rt(120)
        koch(t, x/3)
        t.lt(60)
        koch(t, x/3)

# 5.6.2
def snowflake(t, x):
    """Draw a snowflake using three koch curves
    t: Turtle
    x: Koch curve parameter
    """
    # I'll use three identical Koch curves, so this'll be an equilateral triangle.
    # The internal angle is 60 degrees, and since we need to make a full turn
    # around the outside as we're drawing, it'll be 180-60=120.
    koch(t, x)
    t.rt(120)
    koch(t,x)
    t.rt(120)
    koch(t,x)

# 5.6.3
def quadratic_island(t, x):
    """Draw a quadratic island
    t: Turtle
    x: parameter that determines size and iterations.
       The island scales down by 18 each time, so x must be at least
       18^(n-1) to do n iterations
    """
    if x<18:
        t.fd(x)
    else:
        # Surely there's a more efficient way to write this.
        quadratic_island(t, x/18)
        t.lt(90)
        quadratic_island(t, x/18)
        quadratic_island(t, x/18)
        t.rt(90)
        quadratic_island(t, x/18)
        quadratic_island(t, x/18)
        t.rt(90)
        quadratic_island(t, x/18)
        t.rt(90)
        quadratic_island(t, x/18)
        t.lt(90)
        quadratic_island(t, x/18)
        t.lt(90)
        quadratic_island(t, x/18)
        
        quadratic_island(t, x/18)
        t.rt(90)
        quadratic_island(t, x/18)
        t.rt(90)
        quadratic_island(t, x/18)
        t.lt(90)
        quadratic_island(t, x/18)
        t.lt(90)
        quadratic_island(t, x/18)
        quadratic_island(t, x/18)
        t.lt(90)
        quadratic_island(t, x/18)
        quadratic_island(t, x/18)
        t.rt(90)
        quadratic_island(t, x/18)

        
        


    
# Test the koch function(s)
def test_koch():
    bob = turtle.Turtle()
    #koch(bob, 100)
    #snowflake(bob, 300)
    quadratic_island(bob, 18**3)
    turtle.mainloop()
    
test_koch()
