from poker.validators import RankValidator
class FourOfAKindValidator(RankValidator):
    def __init__(self,cards):
        self.cards = cards
        self.name = "Four Of A Kind"

    def is_valid(self):
        return len(self._count_rank_groups(group_size=4)) == 1

    def best_cards(self):
        rank_with_4_cards = self._count_rank_groups(group_size=4) #{"4":4}
        cards = [
            card
            for card in self.cards
            if card.rank in rank_with_4_cards
        ]
        return cards
        
