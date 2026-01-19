import unittest
from poker.validators import StraightFlushValidator
from poker.card import Card
class TestStraightFlushValidator(unittest.TestCase):
    def setUp(self):
        self.three_of_hearts = Card(rank = "3",suit = "Hearts")
        self.four_of_hearts = Card(rank = "4",suit =  "Hearts")
        self.five_of_hearts = Card(rank = "5",suit =  "Hearts")
        self.six_of_hearts = Card(rank = "6",suit =  "Hearts")
        self.seven_of_hearts = Card(rank = "7",suit =  "Hearts")
        self.eight_of_hearts = Card(rank = "8", suit = "Hearts")

    def test_determines_there_are_not_five_consecutive_cards_with_same_suit(self):
        """
        we have straight and flush but not straight flush in the below example
        """
        cards = [
            self.three_of_hearts,
            self.four_of_hearts,
            self.five_of_hearts,
            self.six_of_hearts,
            Card(rank = "7", suit = "Clubs"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        
        validator = StraightFlushValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            False
            )
    def test_determines_there_are_five_consecutive_cards_with_same_suit(self):
        cards = [
            self.three_of_hearts,
            self.four_of_hearts,
            self.five_of_hearts,
            self.six_of_hearts,
            self.seven_of_hearts,
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Diamonds")
        ]
        
        validator = StraightFlushValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            True
            )

    def test_returns_straight_flush_cards_from_card_collections(self):
        cards = [
            self.three_of_hearts,
            self.four_of_hearts,
            self.five_of_hearts,
            self.six_of_hearts,
            self.seven_of_hearts,
            Card(rank = "King", suit = "hearts"),
            Card(rank = "Ace", suit = "Diamonds")
            ]
        validator = StraightFlushValidator(cards = cards)
        self.assertEqual(
            validator.best_cards(),
            [
            self.three_of_hearts,
            self.four_of_hearts,
            self.five_of_hearts,
            self.six_of_hearts,
            self.seven_of_hearts,
            ]
        )

    def test_returns_straight_flush_cards_from_card_collections(self):
        cards = [
            self.three_of_hearts,
            self.four_of_hearts,
            self.five_of_hearts,
            self.six_of_hearts,
            self.seven_of_hearts,
            self.eight_of_hearts,
            Card(rank = "Ace", suit = "Diamonds")
            ]
        validator = StraightFlushValidator(cards = cards)
        
        self.assertEqual(
            validator.best_cards(),
            [
            # self.three_of_hearts,
            self.four_of_hearts,
            self.five_of_hearts,
            self.six_of_hearts,
            self.seven_of_hearts,
            self.eight_of_hearts
            ]
        )



