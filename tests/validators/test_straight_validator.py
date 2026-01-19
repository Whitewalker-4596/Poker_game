import unittest
from poker.card import Card
from poker.validators import StraightValidator
class TestStraightValidator(unittest.TestCase):
    def setUp(self):
        self.seven = Card(rank = "7",suit =  "Spades")
        self.eight = Card(rank = "8",suit =  "Diamonds")
        self.nine = Card(rank = "9",suit =  "Clubs")
        self.ten = Card(rank = "10",suit =  "Diamonds")
        self.jack = Card(rank = "Jack",suit =  "Hearts")
        self.cards = [
            Card(rank = "2",suit = "Hearts"),
            Card(rank = "6",suit =  "Hearts"),
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack
        ]

    def test_validates_the_cards_have_straight(self):
        validator = StraightValidator(cards = self.cards)
        self.assertEqual(
            validator.is_valid(),
            True
            )
    def test_does_not_say_2_cards_is_straight(self):
        cards = [
            self.seven,
            self.eight
        ]
        validator = StraightValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            False
            )

    def returns_straight_cards_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        self.assertEqual(
            validator.best_cards(),
            [
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack
            ]
        )