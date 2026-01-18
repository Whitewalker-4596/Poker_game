import unittest
from poker.card import Card
from poker.validators import ThreeOfAKindValidator
class TestThreeOfAKindValidator(unittest.TestCase):
    def setUp(self):
        self.king_of_clubs    = Card(rank = "King", suit = "Clubs")
        self.king_of_diamonds = Card(rank = "King", suit = "Diamonds")
        self.king_of_hearts    = Card(rank = "King", suit = "Hearts")
        self.cards = [
            Card(rank = "4", suit = "Diamonds"),
            Card(rank = "6", suit = "Diamonds"),
            self.king_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts
        ]

    def test_validates_the_cards_have_three_of_a_kind(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        self.assertEqual(
            validator.is_valid(),
            True
            )
    
    def returns_three_of_a_kind_cards_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)
        self.assertEqual(
            validator.best_cards(),
            [
            self.king_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts
            ]
        )