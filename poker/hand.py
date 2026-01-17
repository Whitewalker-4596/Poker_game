
class Hand():

    def __init__(self,cards):
        copy = cards[:] #sorting without mutating recieved list
        copy.sort()
        self.cards = copy
        
        self._rank_validations_from_best_to_worst = (
        ("Royal Flush",self._royalflush),
        ("Straight Flush",self._straightflush),
        ("Four of a Kind",self._fourofakind),
        ("Full House",self._fullhouse),
        ("Flush",self._flush),
        ("Straight",self._straight),
        ("Three of a Kind",self._three_of_a_kind),
        ("Two Pair",self._two_pair),
        ("Pair",self._pair),
        ("High Card",self._high_Card),
        ("Empty Hand",self._emptyhand)
        )

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
        return self._straight() and self._flush()
            
    def _fourofakind(self):
        return self._count_rank_groups(group_size=4) == 1
    def _fullhouse(self):
        return self._three_of_a_kind() and self._pair()
            
    def _flush(self):
        for suit_count in self._card_suit_counts.values():
            if suit_count >= 5:
                return True
        return False
    def _straight(self):
        rank_indexes = list(set([card.rank_index for card in self.cards]))
        for i in range(len(rank_indexes)-4):
            is_straight = rank_indexes[i] + 4 == rank_indexes[i+4]
            if is_straight:
                return True
            else:
                continue
        return False

    def _three_of_a_kind(self):
        return self._count_rank_groups(group_size = 3) == 1
            
    def _two_pair(self):
        return self._count_rank_groups(group_size = 2) == 2
            
    def _pair(self):
        return self._count_rank_groups(group_size = 2) == 1
            
    def _high_Card(self):
        return len(self.cards) >= 2

    def _emptyhand(self):
        return len(self.cards) == 0







