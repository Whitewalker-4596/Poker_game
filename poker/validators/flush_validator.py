from poker.validators import RankValidator
class FlushValidator(RankValidator):
    def __init__(self,cards):
        self.cards = cards
        self.name = "Flush"
    
    def is_valid(self):
        return len(self._count_suit_groups) == 1 # {"ace":5} or {"jack":6}

    def best_cards(self):
        suit_count_dict = self._count_suit_groups # {"ace":5} or {"jack":6}
        suit_count_tuple = list(suit_count_dict.items())[0]
        flush_suit,flush_card_count = suit_count_tuple
        flush_cards = [
            card 
            for card in self.cards
            if card.suit == flush_suit
            ]
        return flush_cards[-5:]

