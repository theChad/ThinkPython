# Exercise 10.1

# Traversing through (possibly arbitrary) nested objects makes me think of recursion.
# I'll use a recursive function to work down through the lists. If the input is a list,
# call nested_sum on each element of the list. In the base case, when the input is no
# longer a list, just return the element. I don't check to make sure the elements are
# valid (in this case any number would do). 

def nested_sum(ints):
    """Returns the sum of a nested list of integers
    ints: nested list of integers
    """
    int_sum = 0
    # Recursive case, if ints is a list then add together the sum of each element
    # of ints (whether or not that element happens to be a list). Calling nested
    # sum on each element should return the nested sum of that list.
    # E.g. for nested_sum([[1,2],[3]]) = nested_sum([1,2]) + nested_sum([3])
    # Then nested_sum([1,2]) = nested_sum(1) + nested_sum(2) = 1 + 2
    # And nested_sum([3]) = nested_sum(3) = 3
    if isinstance(ints, list):
        for nums in ints:
            int_sum += nested_sum(nums)
    # Base case, ints is not a list. It could be anything else, but hopefully we've
    # been passed a list with only numbers (or only strings!) in it. The sum
    # of a single atomic element will just be that element, so return that.
    # E.g. nested_sum(3) = 3.
    # Note that nested_sum([3]) still has a list, so it will call the fuction
    # again on 3. nested_sum([3]) = nested_sum(3) = 3.
    else:
        int_sum = ints
    return int_sum

# Exercise 10.2

def cumsum(t):
    # Initialize cs to be a copy of t
    cs = t[:] 
    for i in range(1,len(cs)):
        # Increment the ith element of cs by the cumlulative sum
        # up to that point. So if we have [1,2,3], we leave 1 as is
        # (note the range in the for loop starts with 1, not zero).
        # Then cs[1], which equals 2, will be incremented by cs[0], which is 1.
        # So cs[1] will now be 3. Next loop, cs[2], which starts as 3, will
        # be incremented by cs[1], which is now 3. So cs[2]=3+3=6
        # cs is now [1,3,6], and we can return it.
        cs[i] += cs[i-1]
    return cs

# Exercise 10.3

def middle(t):
    """Return everything but the first and last elements of t.
    """
    # We can just return the middle slice, leaving out zero and len(t).
    # No need to worry about lists of length 2 or less, because
    # Python slices will return the empty list in most cases where the
    # indices don't make sense.
    return t[1:len(t)-1]

# Exercise 10.4

def chop(t):
    # Here I think it does matter if the list is empty, or only has one element.
    # I'll include two element lists, since those would also end up empty.
    if len(t) < 3:
        del t[:] # Delete the entire list, in place
    else:
        t.pop(0)
        t.pop(-1)
    # Could write return None, but this will also return None. As would no return line.    
    return 

# Exercise 10.5

def is_sorted(t):
    """Predicate, true if t is sorted in ascending order.
    t: list
    """
    # sorted(t) will return a sorted version of t, without changing t.
    # == will compare the two lists to see if their value is the same
    # The is operator would fail here, even if the lists look identical
    # i.e. return (t is sorted(t)) would return false always.
    return t==sorted(t)

# Exercise 10.6

def is_anagram(s,t):
    """True if strings s and t are anagrams.
    """
    # We can use sorted() on a string, which will give a list of characters
    # == will then compare two lists of characters, now sorted.
    return sorted(s)==sorted(t)

# Exercise 10.7

def has_duplicates(t):
    """True if any element occurs multiple times in t
    """
    s = sorted(t) # sorted copy of t
    # Check each element against the following element.
    # Since it's sorted, identical elements will be adjacent.
    # Use range(len(s)-1), since we'll always be checking the next
    # element, so no need to go out to the last element.
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            # Found a duplicate!
            return True
    # If we didn't return True already, there are no duplicates
    return False
