# Section 17.2 exercise

class Time:

    def time_to_int(self):
        return self.second + 60 * (self.minute + 60* self.hour)

# Section 17.5 exercise
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Section 17.6 exercise
    def __str__(self):
        return '(%d,%d)' % (self.x, self.y)

    # Section 17.7 exercise, modified for 17.8
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other[0], self.y + other[1])

    def __radd__(self, other):
        return self.__add__(other)


def test():
    p = Point(3,4)
    q = Point(7,2)
    print("Point p is ", p, ". Point q is ", q, ". Their sum is ", p+q, ".", sep='')
    t1 = (20,30)
    print("t1 is ", t1, ". p + t1 is ", p+t1,". t1 + p is ", t1 + p,".",sep='')
    # Note that when using sum, you need to give it an initial value which is
    # a Point or a tuple.
    # Because that value defaults to zero. Alternatively, you could modify
    # __add__ to accept and int as other.
    print("Testing sum, sum([p,q,t1],(0,0)) =", sum([p,q,t1],(0,0)))

if __name__=='__main__':
    test()
    
