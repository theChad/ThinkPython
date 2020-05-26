# Exercise 6.2
# The Ackermann function


# Guardian to make sure inputs are correct
def is_nonnegative_integer(n):
    return isinstance(n, int) and n>= 0

def ack(m,n):
    """Compute the Ackermann function of m and n
    m and n should be nonnegative integers
    """
    # Guardian to make sure m and n are nonnegative integers
    if not (is_nonnegative_integer(m) and is_nonnegative_integer(n)):
        print("m and n must be nonnegative integers.")
        return
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

#print(ack(3,4)) #125
#print(ack(4,4)) #maximum recursion depth exceeded
