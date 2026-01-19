from poker.validators import RankValidator
class PairValidator(RankValidator):
    def __init__(self,cards):
        self.cards = cards
        self.name = "Pair"

    def is_valid(self):
        rank_with_pairs = self._count_rank_groups(group_size = 2) #{"Ace":2}
        return len(rank_with_pairs) == 1

    def best_cards(self):
        rank_with_pairs = self._count_rank_groups(group_size = 2)
        cards = [card for card in self.cards if card.rank in rank_with_pairs]
        return cards