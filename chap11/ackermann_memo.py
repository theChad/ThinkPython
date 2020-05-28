# Exercise 11.3
# The Ackermann function

# Memo dictionary
known = dict()

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
    # m==0 case, just doing an addition so don't worry about looking it up
    if m==0:
        return n+1
    # Using tuples as key. Briefly mentioned (but not really described) in
    # chapter 11, tuples are an immutable list. So they are hashable, unlike
    # normal lists.
    if (m,n) in known:
        return known[(m,n)]
    # Book's solution doesn't memoize this one, possibly because you'll only
    # go down one more level before reaching something you do memoize. 
    elif m>0 and n==0:
        res = ack(m-1,1)
        known[(m,n)] = res
        return res
    # Most of the memoization will occur here.
    elif m>0 and n>0:
        res = ack(m-1,ack(m,n-1)) # store result so we only compute once
        known[(m,n)] = res # memo
        return res

# Function to compute ack(3,n) from formula to check
# the ack function
def ack_3(n):
    """Use formula for ack(3,n)
    """
    return 2**(n+3)-3

print(ack(3,4))
print(ack(3,6))
