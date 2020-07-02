# Section 19.4 Exercise
# Use 'all' fuction for uses_all from 9.3

def uses_all(word, required):
    """True if word uses all letters in required.
    word, required: strings (or any collection)
    """
    # required comes last, because that's the string we want
    # to run through in its entirety. The first part just checks
    # if the letter is in word. If we wrote (letter in required for letter in word)
    # instead, it would ensure that every letter in word was found in required.
    # But there may be some letters in required we didn't check for inclusion in word.
    return all(letter in word for letter in required)

# Section 19.5 Exercise
# Use sets for avoid from 9.3

def avoids(word, forbidden):
    """True if word contains no letters from forbidden.
    word, forbidden: strings (or any collection)
    """
    # Looking at the set documentation, & is set intersection.
    # Taking the intersection shows the common elements, if any
    # If there are any common elements, we want to return False.
    # So negate the truthiness of the intersection. (As a boolean, a set
    # is false only if it's empty.)
    # return not set(word) & set(forbidden)

    # Using only methods shown in the book, we could just use set difference.
    # Subtracting forbidden from word would have no effect if there are no common letters.
    return set(word) == set(word) - set(forbidden)

# Section 19.7 Exercise
# Rewrite has_straightflush using defaultdict
# Just including the snippet for the method; this code won't run here

from collections import defaultdict
def has_straightflush(self):
    """Checks whether this hand has a straight flush.

    Better algorithm (in the sense of being more demonstrably
    correct).
    """
    # partition the hand by suit and check each
    # sub-hand for a straight

    # Make d a defaultdict instead of normal dict
    # The factory will be PokerHand. That just means that
    # if d[key] fails (there's not key named 'key' yet in d),
    # it will assign d[key]=PokerHand(). You give it the factory
    # as a function, then it knows to call that function and
    # assign the return value to d[key].
    d = defaultdict(PokerHand)
    
    for c in self.cards:
        # This line is much cleaner now. Just d[c.suit] is either
        # a PokerHand we've already added cards to, or it's a newly
        # created PokerHand, via the constructor function PokerHand().
        d[c.suit].add_card(c)

    # see if any of the partitioned hands has a straight
    for hand in d.values():
        if len(hand.cards) < 5:
            continue            
        hand.make_histograms()
        if hand.has_straight():
            return True
    return False
