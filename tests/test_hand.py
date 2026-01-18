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

     
    def test_flush_is_best_rank(self):
        cards = [
            Card(rank = rank,suit = "Hearts")
            for rank in ["2","King","4","Jack","Ace"]
        ]
        hand = Hand()
        hand.add_cards(cards = cards)
        self.assertEqual(hand.best_rank(),"Flush")
    def test_fullhouse_is_best_rank(self):
        cards = [
            Card("2","Hearts"),
            Card("3", "Hearts"),
            Card("2", "Spades"),
            Card("2", "Diamonds"),
            Card("3", "Clubs")
        ]
        hand = Hand()
        hand.add_cards(cards = cards)
        self.assertEqual(
            hand.best_rank(),"Full House"
        )

    def test_fourofakind_is_best_rank(self):
        cards = [
            Card("2","Hearts"),
            Card("3", "Hearts"),
            Card("2", "Spades"),
            Card("2", "Diamonds"),
            Card("2", "Clubs")
        ]
        hand = Hand()
        hand.add_cards(cards = cards)
        self.assertEqual(
            hand.best_rank(),"Four of a Kind"
        )
    def test_straightflush_is_best_rank(self):
        cards = [
            Card("3","Hearts"),
            Card("4", "Hearts"),
            Card("6", "Hearts"),
            Card("7", "Hearts"),
            Card("5", "Hearts")
        ]
        hand = Hand()
        hand.add_cards(cards = cards)
        self.assertEqual(
            hand.best_rank(),"Straight Flush"
        )
    def test_royalflush_is_best_rank(self):
        cards = [
            Card("10","Hearts"),
            Card("Jack", "Hearts"),
            Card("King", "Hearts"),
            Card("Queen", "Hearts"),
            Card("Ace", "Hearts")
        ]
        hand = Hand()
        hand.add_cards(cards = cards)
        self.assertEqual(
            hand.best_rank(),"Royal Flush"
        )