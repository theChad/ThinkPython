# Exercise 7.1
import math

def mysqrt(a, epsilon=0.0000000000000001):
    """Uses Newton's Method to return an estimate of sqrt(a)
       a: nonnegative number
       epsilon: final step size/accuracy
    """
    if a<0:
        print("a must be nonnegative.")
        return
    x=a/2
    while True:
        #print(x)
        y = (x + a/x) / 2
        # Instead of checking to see if x=y, use epsilon to avoid
        # floating point representation issues
        if abs(y-x) < epsilon:
            break
        x = y
    return x

def test_square_root():
    """Test the my_sqrt function by computing the square roots of the
    first nine integers and comparing that to python's math.sqrt.
    """
    # Print out the header rows
    print("a   mysqrt(a)          math.sqrt(a)       diff")
    print("-   ---------          -------------      ----")
    a=1.0 # Make a floating point, we'll cycle through it
    while a<10:
        # Store the square root estimates so we don't have to call these
        # functions multiple times for every a
        mysqrt_a=mysqrt(a)
        mathsqrt_a=math.sqrt(a)
        
        # Strings of spaces for padding out each entry. Since the square roots
        # are floating point numbers, we don't necessarily know how many
        # decimal places they'll have. There are other ways to format
        # decimals that will probably be covered later, but for now I'll
        # just pad it out so every number takes up 19 characters (max of 18
        # plus one space). From seeing printouts of testing mysqrt above,
        # Python seems to default to a max of 16 digits after the decimal
        # point, so 18 total characters (for numbers less than 10).

        # str(x) converts x to a string, so we can do things like check
        # its length.
        mysqrt_padding = (19-len(str(mysqrt_a)))*' '
        mathsqrt_padding = (19-len(str(mathsqrt_a)))*' '

        # Put together a string we want to print out as a row in the table
        table_row = str(a) + ' ' + str(mysqrt_a) + mysqrt_padding \
            + str(mathsqrt_a) + mathsqrt_padding + str(abs(mysqrt_a-mathsqrt_a))
        print(table_row)
        
        a+=1 # Increment a, same as a = a + 1

test_square_root()
