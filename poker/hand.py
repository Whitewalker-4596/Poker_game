from poker.validators import (
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardValidator
)
class Hand():

    def __init__(self):
        # copy = cards[:] #sorting without mutating recieved list
        # copy.sort()
        # self.cards = copy
        self.cards = []
        self._rank_validations_from_best_to_worst = (
        ("Royal Flush",self._royalflush),
        ("Straight Flush",self._straightflush),
        ("Four of a Kind",self._fourofakind),
        ("Full House",self._fullhouse),
        ("Flush",self._flush),
        ("Straight",StraightValidator(cards=self.cards).is_valid),
        ("Three of a Kind",ThreeOfAKindValidator(cards=self.cards).is_valid),
        ("Two Pair",TwoPairValidator(cards=self.cards).is_valid),
        ("Pair",PairValidator(cards=self.cards).is_valid),
        ("High Card",HighCardValidator(cards = self.cards).is_valid),
        ("Empty Hand",NoCardValidator(cards = self.cards).is_valid)
        )
    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self,cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    @property
    def _card_rank_counts(self):
        """
        gives dict like in return from a set of given cards 
        for example if given 5 cards:
        {
        "ace" : 2,
        "3" : 1,
        "King" : 2
        }
        """
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank,0)
            card_rank_counts[card.rank] +=1
        return card_rank_counts
    @property
    def _card_suit_counts(self):
        """
        gives dict like in return from a set of given cards 
        for example if given 5 cards:
        {
        "Spades" : 2,
        "Diamonds" : 1,
        "Clubs" : 2
        }
        """
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit,0)
            card_suit_counts[card.suit] +=1
        return card_suit_counts
    
    def _count_rank_groups(self,group_size):
        times = 0
        for rank_count in self._card_rank_counts.values():
            if rank_count == group_size:
                times+=1
        return times   

    def best_rank(self):
        for rank in self._rank_validations_from_best_to_worst:
            name,validator_func = rank
            if validator_func():
                return name
    def _royalflush(self):
        is_straight_flush = self._straightflush()
        if not is_straight_flush:
            return False
        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal
            
    def _straightflush(self):
        return StraightValidator(cards=self.cards).is_valid() and self._flush()
            
    def _fourofakind(self):
        return self._count_rank_groups(group_size=4) == 1
    def _fullhouse(self):
        return ThreeOfAKindValidator(cards=self.cards).is_valid() and PairValidator(cards=self.cards).is_valid()
            
    def _flush(self):
        for suit_count in self._card_suit_counts.values():
            if suit_count >= 5:
                return True
        return False








