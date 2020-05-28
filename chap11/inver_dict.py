# Exercise 11.2

def invert_dict(d):
    """Return a dictionary whose keys are the values of d, and whose
    values are lists of the corresponding keys of d
    """
    inverse = dict()
    for key in d:
        val = d[key]
        # If val is in inverse, setdefault(val,[]) will just return
        # inverse[val], so this is like saying inverse[val].append(key).
        # If val is *not* in inverse, setdefault will create the key-value
        # pair {val: []}, then return inverse[val] (which is now []).
        # Then we call append(key) on this new inverse[val], which will yield
        # inverse[val]=[key]
        inverse.setdefault(val,[]).append(key)
    return inverse
