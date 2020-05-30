# Section 12.4 Exercise 

def sum_all(*args):
    total = 0
    # args is now a tuple (immutable list), so we can just
    # iterate through it as we woul a list.
    for arg in args:
        total += arg
    return total

# Recursive version just for fun.
def sum_all_recursive(*args):
    # Return zero if no arguments initially.
    # Would otherwise never get here
    if len(args)==0:
        return 0
    if len(args)==1:
        return args[0]
    return args[0] + sum_all_recursive(*args[1:])
