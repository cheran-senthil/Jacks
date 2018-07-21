"""Deck class"""
import random
from .card import Card

class Deck:
    """Class to store a Deck"""
    def __init__(self, shuffle=False, color=True):
        self.color = color
        self.deck = []
        self.reset(shuffle)

    def shuffle(self):
        """Shuffle the Deck"""
        random.shuffle(self.deck)

    def draw(self, i=1):
        """Draw from the Deck"""
        if i > len(self.deck):
            i = len(self.deck)
        cards = self.deck[:i]
        self.deck = self.deck[i:]
        return cards

    def reset(self, shuffle=False):
        """Reset the Deck"""
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
