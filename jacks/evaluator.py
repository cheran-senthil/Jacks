"""Evaluator class"""
from itertools import combinations
from pkg_resources import resource_stream

with resource_stream(__name__, 'hand_rankings.txt') as f:
    DATA = [(line[:-1], i+1) for i, line in enumerate(list(f))]
    HAND_LOOKUP = dict(DATA[10:322] + DATA[1599:])
    FLUSH_LOOKUP = dict(DATA[0:10] + DATA[322:1599])

class Evaluator:
    """Evaluator class to evaluate poker hand ranks"""
    @staticmethod
    def hand_rank(hand):
        """returns hand rank for a given hand"""
        ranks = ''
        suits = set()
        for card in hand:
            suits.add(card.suit)
            ranks += card.rank
        ranks = ''.join(sorted(ranks)).encode('ascii')
        if len(suits) == 1:
            return FLUSH_LOOKUP[ranks]
        return HAND_LOOKUP[ranks]

    @staticmethod
    def best_five(hand):
        """Get best five card poker hand"""
        max_rank = 7463
        for poker_hand in combinations(hand, 5):
            if Evaluator.hand_rank(poker_hand) < max_rank:
                max_rank = Evaluator.hand_rank(poker_hand)
                best_hand = poker_hand
        return best_hand

    @staticmethod
    def evaluator(*hands):
        """return best hand and winning player(s)"""
        max_rank = 7463
        for player, hand in enumerate(hands):
            hand = Evaluator.best_five(hand)
            rank = Evaluator.hand_rank(hand)
            if rank < max_rank:
                max_rank = rank
                best_hands = [hand]
                winning_players = [player]
            elif rank == max_rank:
                best_hands.append(hand)
                winning_players.append(player)
        return best_hands, winning_players
