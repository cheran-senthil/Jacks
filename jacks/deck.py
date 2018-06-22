from .card import Card

import random

class Deck:
    def __init__(self, shuffle=True):
        self.reset(shuffle)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self, n=1):
        cards = self.deck[:n]
        self.deck = self.deck[n:]
        return cards

    def reset(self, shuffle=False):
        self.deck = []
        for suit in ['s', 'h', 'd', 'c']:
            for rank in Card.STR_RANKS:
                self.deck.append(Card(rank+suit))
        if shuffle:
            self.shuffle()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.deck)
