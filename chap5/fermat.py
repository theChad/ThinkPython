# Exercise 5.2

import math

# 4.2.1
def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

# 4.2.2
def fermat_inputs():
    print('Please input positive integers to check Fermat\'s theorem.')
    # Use input to take input from the keyboard, and int() to convert them
    # to integers (otherwise they'll be seen as strings)
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    n = int(input('n: '))
    check_fermat(a, b, c, n)

