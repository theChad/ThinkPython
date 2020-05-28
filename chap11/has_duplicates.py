# Exercise 11.4

def has_duplicates(t):
    d = dict()
    for item in t:
        if item in d:
            return True
        d[item]=""
    return False
