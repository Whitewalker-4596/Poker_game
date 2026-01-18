class RankValidator():

    def _count_rank_groups(self,group_size):  #{"ace":2}
        return {
        rank:rank_count
        for rank,rank_count in self._card_rank_counts.items()
        if rank_count == group_size
        }

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