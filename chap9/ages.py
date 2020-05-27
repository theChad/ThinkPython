# Exercise 9.9
# I think the child is 57, and they're 17-18 years apart

# I really shouldn't rewrite functions, but it's a short one and it's more convenient now.
def is_reverse(word1, word2):
    return word1==word2[::-1]

# After looking at the solutions, this should really cover reversed numbers with two different
# differences, since people without the same birthday n+ years apart will have ages
# separated by n and n+1 every year. I added that into the if statement.
def find_num_reversals(diff):
    """Find all two digit reversed numbers with a certain difference, e.g. all
    palindromes separated by 11.
    """
    i = 0
    count = 0
    while i < 100-diff:
        if is_reverse(str(i).zfill(2), str(i+diff).zfill(2)) or \
           is_reverse(str(i).zfill(2), str(i+diff+1).zfill(2)):
            count += 1
            if count==6:
                # Candidate could also refer to i and i+diff+1, but that'll be clear
                # from the printout
                print("Candidate:", i, "and", i+diff)
        i += 1
    return count


def find_age_diff():
    """Find an age difference with 8 reversals in it
    """
    i = 1
    while i < 100:
        num_reversals = find_num_reversals(i)
        if num_reversals>= 6:
            print("Age difference of",i,"has", num_reversals, "reversals.")
        i += 1


find_age_diff()
