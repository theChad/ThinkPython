import copy

class Time:
    """Time of day
    attributes: hour, minute, second
    """

# Section 16.1 exercise

def print_time(t):
    """Print Time object as hh:mm:ss
    t: Time object
    """
    # Format operator was discussed in chapter 14.3
    print("%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second))

def is_after(t1, t2):
    """True if t1 is after t2
    t1, t2: Time objects
    """
    return (t1.hour > t2.hour and
            t1.minute > t2.minute and
            t1.second > t2.second)

# Section 16.3 exercise

def increment(t, seconds):
    """Increment time
    t: Time ojbect
    seconds: number of seconds
    """
    # divmod was discussed in chapter 12.3. Returns a tuple
    # of integer quotient and remainder
    # This is basically just like normal addition with carrying
    # The remainder is what goes in the current place, and the
    # quotient gets carried over to the next place.
    carryover_minutes, t.second = divmod(seconds + t.second, 60)
    carryover_hours, t.minute = divmod(carryover_minutes + t.minute, 60)
    carryover_days, t.hour = divmod(carryover_hours + t.hour, 24)

def pure_increment(t, seconds):
    """Return new time object, with value t plus seconds
    t: Time object
    seconds: number of seconds
    """
    new_time = copy.copy(t)
    increment(new_time, seconds)
    return new_time

# Section 16.4 exercise

# time_to_int and int_to_time copied from book
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

# Rewrite increment using time_to_int and int_to_time
def increment_int(t, seconds):
    """Increment time t by seconds
    t: Time object
    seconds: number of seconds
    """
    t_int = time_to_int(t)
    new_t_int = t_int + seconds
    new_t = int_to_time(new_t_int)
    # For the pure functional version, could just return new_t.
    # If we want to modify the time passed in, we need something different
    # t = new_t won't work, because that just makes our local
    # t point to a different time. If someone calls
    # increment_int(my_time, my_seconds), my_time would still
    # point to the same time object. But we can change each attribute
    # of t individually, since t points to the same Time object
    # that my_time points to.
    t.hour = new_t.hour
    t.minute = new_t.minute
    t.second = new_t.second

    
# Test functions
def test():
    t1 = Time()
    t1.hour = 4
    t1.minute = 7
    t1.second = 9
    t2 = Time()
    t2.hour = 13
    t2.minute = 34
    t2.second = 54
    print("t1 is ", end='')
    print_time(t1)
    print("t2 is ", end='')
    print_time(t2)
    print("is_after(t1, t2):", is_after(t1, t2))
    second_increments = [60, 90, 180, 7200, 60*60*24]
    for inc in second_increments:
        print("t1 plus another %d seconds is " % inc, end='')
        increment(t1, inc)
        print_time(t1)
        print("t2 plus %d seconds is " % inc, end='')
        print_time(pure_increment(t2, inc))


                   
    
if __name__=='__main__':
    test()
    
