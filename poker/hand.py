from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardValidator
)
class Hand():
    VALIDATORS = (
            RoyalFlushValidator,
            StraightFlushValidator,
            FourOfAKindValidator,
            FullHouseValidator,
            FlushValidator,
            StraightValidator,
            ThreeOfAKindValidator,
            TwoPairValidator,
            PairValidator,
            HighCardValidator,
            NoCardValidator
            )
    def __init__(self):
        self.cards = []

    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self,cards):
        copy = self.cards[:] ##sorting without mutating recieved list
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def best_rank(self):
        for index,klass in enumerate(self.VALIDATORS):
            validator = klass(cards = self.cards)
            if validator.is_valid():
                return (index,validator.name,validator.best_cards())


            









