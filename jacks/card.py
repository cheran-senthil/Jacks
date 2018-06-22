class Card:
    """"""

    PRETTY_SUIT = {'d' : u'\u2666', 'h' : u'\u2665',
                   's' : u'\u2660', 'c' : u'\u2663'}
    SUIT_COLOR = {'d' : '\033[94m%s\033[0m', 'h' : '\033[91m%s\033[0m',
                  's' : '%s', 'c' : '\033[92m%s\033[0m'}

    STR_RANKS = '23456789TJQKA'
    INT_RANKS = map(lambda x: x << 8, range(13))
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

    RANK_TO_INT = dict(zip(list(STR_RANKS), INT_RANKS))
    RANK_TO_PRIME = dict(zip(list(STR_RANKS), PRIMES))
    SUIT_TO_INT = {'s' : 1<<12, 'h' : 2<<12, 'd' : 4<<12, 'c' : 8<<12}

    def __init__(self, card, color=True):
        if len(card) != 2:
            raise ValueError('Invalid Card %s Expected 2 chars' % card)

        self.rank = card[0].upper()
        self.suit = card[1].lower()
        self.color = color

        try:
            self.rank_int = Card.RANK_TO_INT[self.rank]
            self.rank_prime = Card.RANK_TO_PRIME[self.rank]
            self.suit_int = Card.SUIT_TO_INT[self.suit]
        except KeyError:
            raise ValueError('Invalid Card %s' % card)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        card = self.rank + Card.PRETTY_SUIT[self.suit]
        if self.color:
            card = Card.SUIT_COLOR[self.suit] % card
        return card.encode('utf-8')
