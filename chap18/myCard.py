# Card related exercises in chapter 18
# Much of the code is copied from the chapter.


class Card:
    """Represents a standard playing card."""

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


class Deck:

    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    # Section 18.6 exercise
    def sort(self):
        """Sorts cards in deck in place."""
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


    # Exercise 18.2
    def deal_hands(self, num_hands, cards_per_hand):
        """Return a list of hands with cards dealt from the 
        deck.
        num_hands, cards_per_hand: integers
        """
        hands = []
        # I deal out each hand all at once. Could also use another
        # for loop to do a normal deal around the table.
        for i in range(num_hands):
            hand = Hand()
            self.move_cards(hand, num_cards)
            hands.append(hand)
        return hands
        
class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.label = label


