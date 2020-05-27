# Exercise 10.10

def in_bisect(s,target):
    """Returns true if target is in sorted list.
    s: sorted list
    target: item to search for
    """
    # Base case, down to one element.
    if len(s)==1:
        if s[0] == target:
            return True
        return False
    if s[0] <= target <= s[-1]:
        mid_index = int(len(s)/2)
        mid = s[mid_index]
        if target < mid:
            return in_bisect(s[:mid_index], target)
        else:
            return in_bisect(s[mid_index:], target)
    return False
