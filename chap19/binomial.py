# Exercise 19.1

def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number of successes

    returns: int
    """
    # Just put all three return possibilities into one statement. Could use parentheses if it
    # seems clearer.
    return 1 if k==0 else 0 if n==0 else binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)

