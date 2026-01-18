import unittest
from poker.card import Card
from poker.validators import HighCardValidator
class TestHighCardValidator(unittest.TestCase):
    def test_validates_the_cards_have_the_high_card(self):
        cards = [
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds")
        ]
        validator = HighCardValidator(cards)
        self.assertEqual(
            validator.is_valid(),
            True
        )
    def test_returns_high_card_from_card_collection(self):
        ace = Card(rank = "Ace",suit =  "Clubs")
        cards = [
            Card(rank = "3", suit =  "Diamonds"),
            Card(rank = "6", suit =  "Spades"),
            Card(rank = "9", suit = "Hearts"),
            Card(rank = "Jack", suit =  "Hearts"),
            ace
        ]
        validator = HighCardValidator(cards)
        self.assertEqual(
            validator.best_cards(),
            [ace]
        )

