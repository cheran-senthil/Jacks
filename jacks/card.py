import six

@six.python_2_unicode_compatible
class Card:
    """"""

    PRETTY_SUIT = {'d' : u'\u2666', 'h' : u'\u2665',
                   's' : u'\u2660', 'c' : u'\u2663'}
    SUIT_COLOR = {'d' : '\033[94m%s\033[0m', 'h' : '\033[91m%s\033[0m',
                  's' : '%s', 'c' : '\033[92m%s\033[0m'}

    def __init__(self, card, color=True):
        """Create a new Card"""
        if len(card) != 2:
            raise ValueError('Invalid Card %s Expected only 2 chars' % card)

        self.rank = card[0].upper()
        self.suit = card[1].lower()
        self.color = color

        if card[0] not in '23456789TJQKA':
            raise ValueError('Invalid Rank %s Expected from 23456789TJQKA' % card[0])
        if card[1] not in 'shdc':
            raise ValueError('Invalid Suit %s Expected s, h, d or c' % card[1])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        card = self.rank + Card.PRETTY_SUIT[self.suit]
        if self.color:
            card = Card.SUIT_COLOR[self.suit] % card
        return card
