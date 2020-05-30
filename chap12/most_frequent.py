# Exercise 12.1


# From Exercise 11.2, just to avoid importing
def invert_dict(d):
    """Return a dictionary whose keys are the values of d, and whose
    values are lists of the corresponding keys of d
    """
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[]).append(key)
    return inverse


def most_frequent(s):
    """Return the letters in s in order of frequency, high to low.
    I return the letters as a string.
    s: string
    """
    hist=dict()
    # Create dictionary mapping letter to frequency
    for c in s:
        hist[c] = hist.get(c,0) + 1
    # Create a dictionary mapping frequency to letter
    freqs = invert_dict(hist)
    # Return letters in order of frequency
    frequent_letters = ''
    for frequency in sorted(freqs, reverse=True):
        for letter in freqs[frequency]:
            frequent_letters += letter
    return frequent_letters
