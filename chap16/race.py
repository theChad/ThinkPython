import my_time

# Exercise 16.7

def mul_time(t, mul):
    """Return the result of multiplying t my mul. Does not modify t.
    t: Time object
    mul: number
    """
    return int_to_time(my_time.time_to_int(t) * mul)

def race_pace(t, dist):
    """Return pace time of race given finishing time and distance.
    t: Time object, finishing time of race
    dist: distance of race
    """
    assert dist >= 0, 'race_pace distance must be >= 0.'
    return mul_time(t, 1/dist)

def test():
    t1 = my_time.Time()
    t1.hour = 3
    t1.minute = 3
    t1.second = 34
    d1 = 26.22
    pace1 = race_pace(t1,d1)
    print("For %f, total time and pace were:" % d1)
    my_time.print_time(t1)
    my_time.print_time(pace1)

if __name__=='__main__':
    test()
