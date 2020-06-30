# Exercise 18.3
# Code downloaded from book and updated to add required features

"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""
    
    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that papear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
            
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_kind(self, n):
        """Returns True if the hand has n of a kind.
        n: integer
        """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= n:
                return True
        return False

    def has_pair(self):
        """Returns True if the hand has a pair"""
        return self.has_kind(2)

    def has_two_pair(self):
        """Returns True if the hand has two pair"""        
        self.rank_hist()
        pairs = 0
        for val in self.ranks.values():
            if val>=2:
                pairs += 1
        return pairs >= 2
    
    def has_three_of_a_kind(self):
        """Returns True if the hand has three of a kind"""        
        return self.has_kind(3)

    def has_straight(self):
        """Returns True if the hand has a straight"""        
        self.rank_hist()
        sorted_ranks = sorted(self.ranks)
        # Make sure Ace counts as low and high
        if sorted_ranks[0]==1:
            sorted_ranks.append(14)
        num_ranks = len(sorted_ranks)
        straight = 1 # keep track of length of straight
        for i in range(num_ranks-1):
            if sorted_ranks[i+1] - sorted_ranks[i] == 1:
                # The next rank is up one from the previous, so
                # the straight is one longer
                straight += 1
                if straight >= 5:
                    # If we've reached 5, we're done
                    return True
            else:
                # Next card isn't part of the straight, so reset
                straight = 1
        # If we made it here, we didn't find any straights
        return False

    # Sort the quantities of all the ranks. If the highest
    # is at least three, and the second highest at least 2,
    # there is at least one full house.
    def has_full_house(self):
        """Returns True if the hand has a full house"""        
        self.rank_hist()
        sorted_values = sorted(self.ranks.values())
        return sorted_values[-1]>=3 and sorted_values[-2]>=2
    
    def has_four_of_a_kind(self):
        return self.has_kind(4)

    # If this were just looking at five card hands, we could
    # just write return self.has_flush() and self.has_straight()
    # But since we can have more cards, that doesn't work.
    def has_straight_flush(self):
        """Returns True if the hand has a straight flush"""        
        suited_hands = {}
        # Build up a dictionary of suited hands. The keys
        # will be the suits, and each vaule will be a Hand with only that suit.
        for card in self.cards:
            suited_hands.setdefault(card.suit,PokerHand()).add_card(card)

        # Search each suited hand for a straight. If there is a straight, it must
        # be a straight flush, so return True.
        for suit in suited_hands:
            if suited_hands[suit].has_straight():
                return True
        return False # Didn't find any straight in the suited hands

    # Classifications, in order from highest to lowest value
    classifications = ["straight flush" , "four of a kind",
                       "full house", "flush",
                       "straight", "three of a kind",
                       "two pair", "pair"]

    # Dictionary of classification tests
    class_tests = {"straight flush": has_straight_flush, "four of a kind":has_four_of_a_kind,
                       "full house":has_full_house, "flush":has_flush,
                       "straight":has_straight, "three of a kind":has_three_of_a_kind,
                       "two pair":has_two_pair, "pair":has_pair}

    # This function works using something called dispatching. I'm not sure if this is the
    # canonical way of doing it, but it's the way that I thought of.
    # It's a way of executing different functions based on input. In this case,
    # the input will be the name of the classification (like "two pair").
    # I have a dictionary whose values are functions (since we can use functions
    # as data). So self.class_tests["two pair"] will return the function has_two_pair.
    # I can't run this the normal way, since self.self.class_tests["two pair"] will
    # look for an attributed called self in PokerHand, which we don't have.
    # But that's okay, because self.has_two_pair() is just a shortcut for
    # PokerHand.has_two_pair(self). Since we're in PokerHand, we can leave that bit out
    # and just write has_two_pair(self). And since self.class_tests["two pair"] returns
    # has_two_pair, we can write self.class_tests["two pair"](self), and it will be as if
    # we'd run self.has_two_pair().
    #
    # I think this is a cleaner, more succinct way of doing things. But you could also do
    # dispatching using a separate function and if statements. Or even forgo the separate
    # function and just do it all in classify, running through the test functions one by
    # one and returning as soon as you get a hit.
    #
    # The book does it a slightly cleaner way using getattr, however the final calculations
    # aren't quite what are implied by the question in the book. The book's solutions
    # count *all* classifications of a hand, not just the highest value.
    def classify(self):
        """Returns the highest-value classification for a hand."""
        for classification in self.classifications:
            if self.class_tests[classification](self):
                self.label = classification
                return classification
        self.label = None
        return None


def count_deck_classifications(class_counts):
    """Return histogram of classifications from dealing out one deck.
    class_counts: starting histogram
    """
    deck = Deck()
    deck.shuffle()
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand,7)
        hand_class = hand.classify()
        class_counts[hand_class] = class_counts.get(hand_class,0) + 1


def count_many_classifications(n=10000):
    """Return histogram of classifications across dealing out n decks
    n: number of decks
    """
    class_counts = {}
    for i in range(n):
        count_deck_classifications(class_counts)
    return class_counts

def hand_rankings(class_counts):
    """Print a table of the probability of various hands
    class_counts: histogram of hand classifications
    """
    total = sum(class_counts.values())
    print("Prob  ", "Classification")
    print("------", "--------------")
    for classification in PokerHand.classifications + [None]:
        # In looking up the format operator again, I saw that Python now prefers using
        # str.format to %-formatting. The stuff inside the curly braces is a format string
        # for the first (and only, here) argument to format. : is sort of the replacement for %.
        # >6 tells it to right-justify within 6 spaces, and .2% tells it to display
        # as a percenage, with two digits after the decimal.
        print("{:>6.2%}".format(class_counts.get(classification,0)/total), classification)


if __name__ == '__main__':
    # Compute probabilities
    hand_rankings(count_many_classifications())
    
