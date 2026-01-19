
from poker.validators import StraightFlushValidator
class RoyalFlushValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = "Royal Flush"
    
    def is_valid(self):
        straight_flush_validator = StraightFlushValidator(self.cards)
        if straight_flush_validator.is_valid():
            cards = straight_flush_validator.best_cards()
            # print(cards)
            is_royal = cards[-1].rank == "Ace"
            return is_royal
            
        return False

    def best_cards(self):
        return StraightFlushValidator(self.cards).best_cards()
    






    # def is_valid(self):
    #     straight_flush_cards = StraightFlushValidator(self.cards).best_cards()
    #     for card in straight_flush_cards:
    #         if card.rank == "Ace":
    #             return True

    #     return False

    # def best_cards(self):
    #     straight_flush_cards = StraightFlushValidator(self.cards).best_cards()
    #     return straight_flush_cards



