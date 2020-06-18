# Exercise 16.2

import datetime

# Exercise 16.2.1

def weekday_name(weekday_num):
    """Return a string, name of weekday, given the number.
    Monday is 0, Sunday is 6.
    """
    names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
             'Friday', 'Saturday', 'Sunday']
    return names[weekday_num]

def day_of_week():
    """Print the current day of the week
    """
    # From the documentation, the date type has a class method today()
    # which returns a date object with today's value. The fact that it' a
    # class method basically just means it's a function at the top level
    # of that module. You don't have to reference a specific date object.
    # You can just use date.today(). But since date is in the datetime module,
    # you need datetime.date.today().
    # weekday() is a 'normal' object method, which means you have to call it on
    # a date object. So datetime.date.weekday() won't work. You have to have
    # <date object>.weekday(). Since datetime.date.today() returns a
    # date object, we can call weekday on the result of that like this:
    # datetime.date.today().weekday().
    print(weekday_name(datetime.date.today().weekday()))

# Exercise 16.2.2

# I used datetime.datetime here, instead of datetime.date, because
# we also want the time until their birthday.
# The distinction between datetime and datetime.datetime can be confusing,
# but it's similar to things I've done before here. datetime is a module
# (datetime.py is a file), and datetime is a class defined in that module.
# So datetime.datetime is like when I typed my_time.Time(). If I just type
# Time(), python will be confused because there's no Time() object or function
# in the file we're in now. my_time.Time() tells it to look in my_time.py.
# Simliarly, datetime.today() would be confusing for a slightly different
# reason - there's no method called today() at the top level of datetime.py.
# It only makes sense as a method of datetime *within* datetime.py.
# If you had a Point object my_point, with x and y coordinates, and then
# tried to do print(x) instead of print(my_point.x), you'd run into the same issue.
# Python needs to know where to look for x.

def time_till_birthday(birthday):
    """Return the time until the next birthday
    birthday: datetime object
    """
    today = datetime.datetime.today()
    # Start with a guess that the next birthday is this year
    next_birthday = birthday.replace(year=today.year)
    # If it's already passed this year, set next_birthday to next year
    if next_birthday < today:
        next_birthday = birthday.replace(year=today.year+1)
    age = next_birthday.year - birthday.year - 1
    time_remaining = next_birthday - today
    print('You are', age, 'years old.')
    print('Time until next birthday:', time_remaining)
    return next_birthday - today

# Exercise 16.2.3, 16.2.4

def double_day(bday_1, bday_2, n=2):
    """Return the day when one person is twice as old as the other,
    given their birthdays. Optionally find when one person is n times older.
    bday_1, bday_2: date (or datetime) objects. Must be the same type.
    n: number, > 1
    """
    # Double day will be when the younger person's age is the
    # same as their difference in age.
    # The n-1 factor will just be 1 and have no effect if we're
    # doubling (n=2).
    # younger = older - diff. So if older = n * younger,
    # younger = n*younger - diff ==> younger = diff/(n-1).
    # So we just need the date when younger's age is diff/(n-1).
    diff = abs(bday_2 - bday_1)
    return max(bday_1, bday_2) + diff / (n-1)

if __name__=='__main__':
    day_of_week()
    birthday = datetime.datetime(1835, 11, 30)
    print("Time till next birthday: ", end='')
    time_till_birthday(birthday)
    birthday2 = datetime.datetime(1860, 11, 30)
    dday = double_day(birthday, birthday2)
    print("Double day is", dday)
    tday = double_day(birthday, birthday2, 3)
    print("Triple day is", tday)
