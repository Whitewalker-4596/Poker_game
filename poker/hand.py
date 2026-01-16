
class Hand():

    def __init__(self,cards):
        self.cards = cards
        self._rank_validations_from_best_to_worst = (
        ("Straight",self._straight),
        ("Three of a Kind",self._three_of_a_kind),
        ("Two Pair",self._two_pair),
        ("Pair",self._pair),
        ("High Card",self._high_Card)
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

    def best_rank(self):
        for rank in self._rank_validations_from_best_to_worst:
            name,validator_func = rank
            if validator_func():
                return name

    def _three_of_a_kind(self):
        return self._count_rank_groups(group_size = 3) == 1
            
    def _two_pair(self):
        return self._count_rank_groups(group_size = 2) == 2
            
    def _pair(self):
        return self._count_rank_groups(group_size = 2) == 1
            
    def _high_Card(self):
        return True

    def _count_rank_groups(self,group_size):
        times = 0
        for rank_count in self._card_rank_counts.values():
            if rank_count == group_size:
                times+=1
        return times   




