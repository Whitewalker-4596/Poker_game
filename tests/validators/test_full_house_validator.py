import unittest
from poker.validators import FullHouseValidator
from poker.card import Card
class TestFullHouseValidator(unittest.TestCase):
    def setUp(self):
        self.four_of_clubs = Card(rank = "4",suit = "Clubs")
        self.four_of_hearts = Card(rank = "4",suit = "Hearts")
        self.four_of_spades = Card(rank = "4",suit = "Spades")
        self.jack_of_diamonds = Card(rank = "Jack",suit = "Diamonds")
        self.jack_of_spades = Card(rank = "Jack",suit = "Spades")

        self.cards = [
            Card(rank = "2", suit = "Spades"),
            self.four_of_clubs,
            self.four_of_hearts,
            self.four_of_spades,
            Card(rank = "5",suit = "Clubs"),
            self.jack_of_diamonds,
            self.jack_of_spades
        ]

    def test_validates_cards_have_full_house(self):
        validator = FullHouseValidator(cards = self.cards)
        self.assertEqual(
            validator.is_valid(),
            True
            )

    def test_returns_fullhouse_cards_from_card_collections(self):
        validator = FullHouseValidator(cards = self.cards)
        self.assertEqual(
            validator.best_cards(),
            [
            self.four_of_clubs,
            self.four_of_hearts,
            self.four_of_spades,
            self.jack_of_diamonds,
            self.jack_of_spades
            ]
        )
