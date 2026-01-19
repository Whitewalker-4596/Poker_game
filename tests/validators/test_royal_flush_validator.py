import unittest
from poker.validators import RoyalFlushValidator
from poker.card import Card
class TestRoyalFlushValidator(unittest.TestCase):
    def setUp(self):
        self.ten_of_hearts = Card(rank = "10",suit = "Hearts")
        self.jack_of_hearts = Card(rank = "Jack",suit =  "Hearts")
        self.queen_of_hearts = Card(rank = "Queen",suit =  "Hearts")
        self.king_of_hearts = Card(rank = "King",suit =  "Hearts")
        self.ace_of_hearts = Card(rank = "Ace",suit =  "Hearts")


    def test_straight_flush_without_same_suit_ace_is_not_royalflush(self):
        cards = [
            Card(rank = "9", suit = "Hearts"),
            self.ten_of_hearts,
            self.jack_of_hearts,
            self.queen_of_hearts,
            self.king_of_hearts,
            Card(rank = "Ace", suit = "Clubs")
        ]
        validator = RoyalFlushValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_straight_flush_with_same_suit_ace_is_royalflush(self):
        cards = [
            Card(rank = "9", suit = "Hearts"),
            self.ten_of_hearts,
            self.jack_of_hearts,
            self.queen_of_hearts,
            self.king_of_hearts,
            self.ace_of_hearts,
            Card(rank = "Ace",suit = "Diamonds")
        ]
        validator = RoyalFlushValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_straight_flush_cards_ends_with_ace(self):
        cards = [
            Card(rank = "9", suit = "Hearts"),
            self.ten_of_hearts,
            self.jack_of_hearts,
            self.queen_of_hearts,
            self.king_of_hearts,
            self.ace_of_hearts,
            Card(rank = "Ace",suit = "Diamonds")
        ]
        validator = RoyalFlushValidator(cards = cards)
        self.assertEqual(
            validator.best_cards(),
            [
            self.ten_of_hearts,
            self.jack_of_hearts,
            self.queen_of_hearts,
            self.king_of_hearts,
            self.ace_of_hearts
            ]
        )