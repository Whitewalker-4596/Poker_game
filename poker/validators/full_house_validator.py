from poker.validators import PairValidator,ThreeOfAKindValidator
class FullHouseValidator():
    def __init__(self,cards):
        self.cards = cards
        self.name = "Full House"

    def is_valid(self):
        return (ThreeOfAKindValidator(cards=self.cards).is_valid() 
                and PairValidator(cards=self.cards).is_valid())
    
    def best_cards(self):
        three_of_a_kind_cards = ThreeOfAKindValidator(self.cards).best_cards() 
        pair_cards = PairValidator(self.cards).best_cards()
        full_house_Cards =  three_of_a_kind_cards  + pair_cards
        full_house_Cards.sort()
        return full_house_Cards

    





