# Exercise 5.3

# 4.3.1
def is_triangle(a, b, c):
    if a>b+c or b>a+c or c>a+b:
        print("No")
    else:
        print("Yes")

# 4.3.2        
def input_triangle():
    print("Enter three side lengths, and I'll tell you if you can make a triangle.")
    # Cast to int, since we're only accepting integer arguments anyway.
    # Could also use float(x) if we wanted to accept decimal arguments.
    # Either way, need to convert them from the strings they'll be read as.
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    is_triangle(a, b, c)

input_triangle()
