import unittest

def product(a,b):
    # result = 0
    # for i in range(a):
    #     result+=b
    # return result
    return a*b

class TestMultiply(unittest.TestCase):
    def test_multiply_two_numbers(self):
        self.assertEqual(product(3,4), 12)

if __name__ == "__main__":
    unittest.main()
# Refactored code

        # for suit in cls.SUITS:
        #     for rank in cls.RANKS:
        #         # cards.append(1)
        #         cards.append(Card(suit = suit,rank = rank))
        # return cards
        
    #defining property insted
    # RANKS_FROM_BEST_TO_WORST = (
    #     "Three of a Kind",
    #     "Two Pair",
    #     "Pair",
    #     "High Card"
    # )

            # refactored into property
        # card_rank_counts = {}
        # for card in self.cards:
        #     card_rank_counts.setdefault(card.rank,0)
        #     card_rank_counts[card.rank] +=1
        
        # count_pairs = 0
        # count_three_of_a_kind = 0
        # for rank_count in self._card_rank_counts.values():
        #     if rank_count == 2:
        #         count_pairs+=1
        #     if rank_count == 3:
        #         count_three_of_a_kind+=1

        # if self._count_rank_groups(group_size = 3) == 1:
        #     return "Three of a Kind"
        # elif self._count_rank_groups(group_size = 2) == 2:        
        #     return "Two Pair"
        # elif self._count_rank_groups(group_size = 2) == 1:
        #     return "Pair"
        # return "High Card" 

        #from straight function
                # rank_indexes = list(set([card.rank_index for card in self.cards]))
        # rank_indexes.sort()
        # count = 0
        # for index,rank_index in enumerate(rank_indexes[:-1]):
            
        #     if rank_index + 1 == rank_indexes[index+1]:
        #         if count >=4:
        #             return count
        #         count +=1
        #     else :
        #         if count >=4:
        #             return count
        #         count = 0
        # if count >= 4:
        #     return True
        # return False