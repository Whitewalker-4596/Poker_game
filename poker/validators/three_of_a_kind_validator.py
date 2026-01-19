from poker.validators import RankValidator
class ThreeOfAKindValidator(RankValidator):
    def __init__(self,cards):
        self.cards = cards
        self.name = "Three Of A Kind"

    def is_valid(self):
        rank_with_pairs = self._count_rank_groups(group_size = 3) #{"Ace":2,"king":2}
        return len(rank_with_pairs) == 1

    def best_cards(self):
        rank_with_3_cards = self._count_rank_groups(group_size = 3)
        cards = [card for card in self.cards if card.rank in rank_with_3_cards]
        return cards
