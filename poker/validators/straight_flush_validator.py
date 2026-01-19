from poker.validators import FiveCardsInARowValidator
class StraightFlushValidator(FiveCardsInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight Flush"
    
    def is_valid(self):
        #[["3","4","5","6","7"]]
        return len(self._straightflush_card_batches) >= 1
    
    def best_cards(self):
        return self._straightflush_card_batches[-1]
         
    @property    
    def _straightflush_card_batches(self):
        return [
            five_cards
            for five_cards in self._collection_of_five_straight_cards_in_a_row
            # {"hearts","hearts","hearts"} => {"hearts"} remove duplicates in below line
            if len({card.suit for card in five_cards}) == 1
        ]

                