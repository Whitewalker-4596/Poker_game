import unittest
from poker.hand import Hand
from poker.card import Card
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

