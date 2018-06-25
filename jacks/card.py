import six
from termcolor import colored

@six.python_2_unicode_compatible
class Card:
    """"""

    PRETTY_SUIT = {'d' : u'\u2666', 'h' : u'\u2665',
                   's' : u'\u2660', 'c' : u'\u2663'}
    SUIT_COLOR = {'d' :  lambda x: colored(x, 'blue'),
                  'h' :  lambda x: colored(x, 'red'),
                  's' : lambda x: x,
                  'c' : lambda x: colored(x, 'green')}

    def __init__(self, card, color=True):
        """Create a new Card"""
        if len(card) != 2:
            raise ValueError('Invalid Card "%s" Expected only 2 chars' % card)

        self.rank = card[0].upper()
        self.suit = card[1].lower()
        self.color = color

        if self.rank not in list('23456789TJQKA'):
            raise ValueError('Invalid Rank "%s" Expected from 23456789TJQKA' % self.rank)
        if self.suit not in list('shdc'):
            raise ValueError('Invalid Suit "%s" Expected s, h, d or c' % self.suit)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        card = self.rank + Card.PRETTY_SUIT[self.suit]
        if self.color:
            card = Card.SUIT_COLOR[self.suit](card)
        return card
