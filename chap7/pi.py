# Exercise 7.3
import math # for sqrt and factorial


def pi_unscaled_term(k):
    """Compute the kth term of the sequence, before being scaled
    by 2*sqrt(2)/9801
    """
    numerator = math.factorial(4*k)*(1103+26390*k)
    denominator = math.factorial(k)**4*396**(4*k)
    return numerator/denominator
    
def estimate_pi(epsilon=1e-15):
    # So we don't have to multiply by the factor at the beginning each time,
    # store it and compute a new epsilon that takes that out.
    # So now the last term has to be smaller than epsilon/scale_factor,
    # and when we multiply the whole thing by scale_factor at the end,
    # the last term will be smaller than (epsilon/scale_factor)*scale_factor,
    # which equals epsilon.
    scale_factor = 2*math.sqrt(2)/9801
    unscaled_epsilon = epsilon/scale_factor
    # Initialize the index
    k=0
    # Get the first term of the sequence
    unscaled_term = pi_unscaled_term(k)
    # Start the summation by setting 1/pi equal to the first (unscaled) term
    unscaled_one_over_pi = unscaled_term
    while unscaled_term >= unscaled_epsilon:
        k += 1 # increment k for the next term in the series
        # Compute the next term in the sequence
        unscaled_term = pi_unscaled_term(k)
        # Add it to our unscaled 1/pi to get the next term in the series
        unscaled_one_over_pi += unscaled_term
    # Compute pi by multiplying our unscaled 1/pi estimate by the scale factor,
    # then dividing 1 by the result. 1/(1/pi) = pi.
    pi = 1/(unscaled_one_over_pi * scale_factor)
    return pi

def test_pi_estimate():
    print(abs(math.pi-estimate_pi()))
    
test_pi_estimate()
        
