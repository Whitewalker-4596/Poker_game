import unittest
from poker.hand import Hand
from poker.card import Card
class TestHand(unittest.TestCase):
    def test_recieves_and_stores(self):
        cards = [
            Card("2","Hearts"),
            Card("7","Diamonds")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(
        hand.cards ,cards
        )
    def test_high_card_is_best_rank(self):
        cards = [
            Card("2","Hearts"),
            Card("7","Diamonds")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(), "High Card")
    def test_pair_is_best_rank(self):
        cards = [
            Card("Ace", "Hearts"),
            Card("Ace", "Diamonds")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank() , "Pair")
    def test_two_pair_is_best_rank(self):
        cards = [
            Card("Ace", "Hearts"),
            Card("Ace", "Diamonds"),
            Card("4", "Diamonds"),
            Card("King", "Clubs"),
            Card("King", "Diamonds")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank() , "Two Pair")

    def test_three_of_a_kind_is_best_rank(self):
        cards = [
            Card("Ace", "Hearts"),
            Card("Ace", "Diamonds"),
            Card("4", "Diamonds"),
            Card("Ace", "Clubs"),
            Card("King", "Diamonds")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(
            hand.best_rank(),"Three of a Kind"
        )
     
    def test_straight_is_best_rank(self):
        cards = [
            Card("5","Hearts"),
            Card("6", "Hearts"),
            Card("2", "Spades"),
            Card("4", "Diamonds"),
            Card("3", "Clubs"),
            Card("5", "Diamonds"),
            Card("King","Hearts")
        ]
        hand = Hand(cards = cards)
        self.assertEqual(
            hand.best_rank(),"Straight"
        )
    def test_flush_is_best_rank(self):
        cards = [
            Card(rank = rank,suit = "Hearts")
            for rank in ["2","King","4","Jack","Ace"]
        ]
        hand = Hand(cards = cards)
        self.assertEqual(hand.best_rank(),"Flush")