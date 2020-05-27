# Exercise 9.7

import words # For the filter function


# Official answer to this question is much cleaner, and a bit more complete.
# I'm just leaving this as it's what I came up with.

def trip_deuce(word):
    """Predicate to determine if word has three consecutive double letters
    """
    count = 0 # Number of double words in a row currently
    i=0 # Position in word
    word = word.lower() # Make it lower case for comparison's sake

    # Run through the word, up through the second to last letter.
    # I'll be checking that against the next letter, so this should cover
    # all letters.
    while i < len(word)-1:
        # Case 1: found a double letter. Add one to the count of double letters
        # and skip the next letter, since it's already part of a pair.
        if word[i]==word[i+1]:
            count += 1
            i += 2
            # If we've reached three already, return true because we're done.
            if count == 3:
                return True
        # Case 2: It doesn't match the next letter, but it does match the previous
        # adjacent pair. This isn't likely to come up, but technically could.
        # Basically just for triple letters, which is pretty rare.
        # I actually ignore the even rarer/unseen quintuple letter instance.
        # Whoops.
        elif count > 0 and word[i]==word[i-1]:
            count = 1
            i += 1
        # Case 3: Not part of a double letter pair at all. Reset the count
        # and go to the next letter.
        else:
            count = 0
            i += 1
    return False
    
def find_trip_deuce_word():
    words.filter_words(trip_deuce)

find_trip_deuce_word()
