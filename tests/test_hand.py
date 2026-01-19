import unittest
from poker.hand import Hand
from poker.card import Card
from poker.validators import PairValidator
class TestHand(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards,[]) 

    def test_representation_of_hand(self):
        cards = [
            Card("3","Hearts"),
            Card("6","Clubs")
        ]
        hand = Hand()
        hand.add_cards(cards = cards)
        self.assertEqual(repr(hand),"3 of Hearts, 6 of Clubs")

    def test_recieves_and_stores(self):
        cards = [
            Card("2","Hearts"),
            Card("7","Diamonds")
        ]
        hand = Hand()
        hand.add_cards(cards = cards)
        self.assertEqual(
        hand.cards ,cards
        )

    #creating the sub class of hand class to test the hand class by giving one validator 
    # insted of all the validators and get the functions of hand by inheritance

    def test_interacts_with_validator_to_get_winninig_hand(self):
        class HandWithOneValidator(Hand):
            #rewriting class argument with one value for testing
            VALIDATORS = (PairValidator,) 

        ace_of_hearts = Card(rank = "Ace",suit = "Hearts")
        ace_of_diamonds = Card(rank = "Ace",suit = "Diamonds")
        three_of_hearts = Card(rank = "3",suit = "Hearts")

        cards = [
            three_of_hearts,
            ace_of_diamonds,
            ace_of_hearts
        ]
        hand = HandWithOneValidator()
        hand.add_cards(cards = cards)
        self.assertEqual(
            hand.best_rank(),
            (0,"Pair",[ace_of_diamonds,ace_of_hearts])
        )


