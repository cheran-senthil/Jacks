from pkg_resources import resource_stream
from itertools import combinations

resource_package = __name__
with resource_stream(resource_package, 'hand_rankings.txt') as f:
    data = [(line[:-1], i+1) for i, line in enumerate(list(f))]
    hand_lookup = dict(data[10:322] + data[1599:])
    flush_lookup = dict(data[0:10] + data[322:1599])

class evaluator:
    def hand_rank(hand):
        ranks = ''
        suits = set()
        for card in hand:
            suits.add(card.suit)
            ranks += card.rank
        ranks = ''.join(sorted(ranks)).encode('ascii')
        if len(suits) == 1:
            return flush_lookup[ranks]
        return hand_lookup[ranks]

    def best_five(hand):
        max_rank = 7463
        best_hand = []
        for poker_hand in combinations(hand, 5):
            if evaluator.hand_rank(poker_hand) < max_rank:
                max_rank = evaluator.hand_rank(poker_hand)
                best_hand = poker_hand
        return best_hand

    def evaluator(*hands):
        max_rank = 7463
        best_hand = []
        winning_player = 0
        for player, hand in enumerate(hands):
            hand = evaluator.best_five(hand)
            rank = evaluator.hand_rank(hand)
            if rank < max_rank:
                max_rank = rank
                best_hand = hand
                winning_player = player
        return best_hand, winning_player
