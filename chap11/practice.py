# Section 11.2 exercise

def histogram(s):
    """Return a dictionary of frequencies of characters in string s
    """
    d = dict()
    for c in s:
        # For every character, add one to the corresponding
        # value in the dictionary. If c is not a key in the dictionary
        # yet, this will create it, and d.get(c,0) will be zero, so
        # d[c] will equal 1.
        d[c] = d.get(c,0) + 1
