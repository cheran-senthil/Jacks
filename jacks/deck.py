from .card import Card

import random

class Deck:
    def __init__(self, shuffle=False, color=True):
        self.color = color
        self.reset(shuffle)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self, n=1):
        if(n > len(self.deck)):
            n = len(self.deck)
        cards = self.deck[:n]
        self.deck = self.deck[n:]
        return cards

    def reset(self, shuffle=False):
        self.deck = []
        for suit in 'shdc':
            for rank in 'A23456789TJQK':
                self.deck.append(Card(rank+suit, color=self.color))
        if shuffle:
            self.shuffle()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.deck)
