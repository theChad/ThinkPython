# Exercise 6.5
import ackermann # for nonnegative integer check

def gcd(a,b):
    if not(ackermann.is_nonnegative_integer(a) or ackerman.is_nonnegative_integer(b)):
        print("Please enter nonnegative integers.")
    if b==0:
        return a
    return gcd(b,a%b) # % is modulo operator, a%b gives remainder of a/b

#print(gcd(27,18))
