# Mid-chapter exercises in chapter 6
import math

# 6.1
def compare(x,y):
    if x>y:
        return 1
    if x==y:
        return 0
    else:
        return -1


# 6.2
def hypotenuse(a,b):
    return math.sqrt(a**2+b**2)

# 6.4
def is_between(x,y,z):
    return x<=y<=z
