
class StraightValidator():
    def __init__(self,cards):
        self.cards = cards
        self.name = "Straight"
    
    def is_valid(self):
        return len(self._collection_of_five_straight_cards_in_a_row) >= 1

    def best_cards(self):
        return self._collection_of_five_straight_cards_in_a_row[-1]
        
    @property
    def _collection_of_five_straight_cards_in_a_row(self):
        index = 0
        rank_indexes = list(set([card.rank_index for card in self.cards]))
        straight_collection = []
        last_card_index = len(rank_indexes) -1
        while index + 4 <= last_card_index:
            next_five_cards = rank_indexes[index:index+5] #last is excluded
            if self._every_element_increasing_by_1(next_five_cards):
                straight_collection.append(next_five_cards)
            index +=1

        return straight_collection


    def _every_element_increasing_by_1(self,rank_indexes):
        start_index = rank_indexes[0]
        # last_index = start_index+4 #no need to be 5 cards
        last_index = rank_indexes[-1]
        straight_consicutive_index = list(range(start_index,last_index+1))
        return rank_indexes == straight_consicutive_index
