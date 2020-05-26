# Section 7.3 exercise

def print_n(s, n):
    """Print a string (s) n times.
    s: string
    n: number of times to print (will be rounded down to nearest integer)
       negative n will not print anything
    """
    while n>=1:
        print(s)
        n-=1 # decrement n; same as n = n-1

print_n('test', 5.5)
print_n('not a test', -34)
