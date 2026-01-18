import unittest
from poker.card import Card
from poker.validators import TwoPairValidator
class TestTwoPairValidator(unittest.TestCase):
    def setUp(self):
        self.king_of_clubs    = Card(rank = "King", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.ace_of_hearts    = Card(rank = "Ace", suit = "Hearts")
        self.ace_of_diamonds  = Card(rank = "Ace", suit = "Diamonds")
        self.cards = [
            Card(rank = "4", suit = "Diamonds"),
            self.king_of_clubs,
            self.king_of_diamonds,
            self.ace_of_diamonds,
            self.ace_of_hearts
        ]

    def test_validates_the_cards_have_atleast_two_pair(self):
        validator = TwoPairValidator(cards = self.cards)
        self.assertEqual(
            validator.is_valid(),
            True
            )
    
    def returns_two_pair_cards_from_card_collection(self):
        validator = TwoPairValidator(cards = self.cards)
        self.assertEqual(
            validator.best_cards(),
            [
            self.king_of_clubs,
            self.king_of_diamonds,
            self.ace_of_diamonds,
            self.ace_of_hearts
            ]
        )