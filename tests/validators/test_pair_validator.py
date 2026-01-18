import unittest
from poker.card import Card
from poker.validators import PairValidator
class TestPairValidator(unittest.TestCase):
    def setUp(self):
        self.ace_of_hearts = Card(rank = "Ace", suit = "Hearts")
        self.ace_of_diamonds = Card(rank = "Ace", suit = "Diamonds")
        self.cards = [
            Card(rank = "3", suit = "Diamonds"),
            Card(rank = "4", suit = "Diamonds"),
            self.ace_of_diamonds,
            self.ace_of_hearts            
        ]

    def test_validates_the_cards_have_pair(self):
        cards = [self.ace_of_diamonds,self.ace_of_hearts]
        validator = PairValidator(cards = cards)
        self.assertEqual(
            validator.is_valid(),
            True
            )
    
    def returns_pair_cards_from_card_collection(self):
        validator = PairValidator(cards = self.cards)
        self.assertEqual(
            validator.best_cards(),
            [
                self.ace_of_diamonds,self.ace_of_hearts
            ]
        )

    