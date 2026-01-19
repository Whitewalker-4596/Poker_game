import unittest
from poker.validators import FourOfAKindValidator
from poker.card import Card
class TestFourOfAKindValidator(unittest.TestCase):
    def setUp(self):
        self.four_of_clubs = Card(rank = "4",suit =  "Clubs")
        self.four_of_diamonds = Card(rank = "4",suit =  "Diamonds")
        self.four_of_hearts = Card(rank = "4",suit = "Hearts")
        self.four_of_spades = Card(rank = "4",suit =  "Spades")

        self.cards = [
            Card(rank="3", suit= "Diamonds"),
            self.four_of_clubs,
            self.four_of_diamonds,
            self.four_of_hearts,
            self.four_of_spades,
            Card(rank = "10",suit =  "Hearts")
        ]

    def test_validates_cards_have_four_of_a_kind(self):
        validator = FourOfAKindValidator(cards = self.cards)
        self.assertEqual(
            validator.is_valid(),
            True
            )

    def test_returns_four_of_a_kind_cards_from_card_collections(self):
        validator = FourOfAKindValidator(cards = self.cards)
        self.assertEqual(
            validator.best_cards(),
            [
            self.four_of_clubs,
            self.four_of_diamonds,
            self.four_of_hearts,
            self.four_of_spades
            ]
        )
        


