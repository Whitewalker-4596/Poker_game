import unittest
from poker.card import Card
class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank,"Queen")
    def test_has_suit(self):
        card = Card(rank = "3",suit = "Clubs")
        self.assertEqual(card.suit,"Clubs")
    def test_has_str_representation_with_rank_and_suit(self):
        card = Card(rank = "Ace",suit = "Spades")
        self.assertEqual(str(card), "Ace of Spades")
    def test_has_technical_representation(self):
        card = Card("5","Diamonds")
        self.assertEqual(repr(card),"Card(rank = '5', suit = 'Diamonds')")
    def test_card_has_4_possible_suits(self):
        self.assertEqual(
            Card.SUITS,
            ("Hearts","Clubs","Spades","Diamonds")
        )
    def test_card_has_13_possible_ranks(self):
        self.assertEqual(
            Card.RANKS,
            ("2","3","4","5","6","7","8","9","10",
            "Jack","Queen","King","Ace")
        )
    def test_incorrect_rank_name(self):
        with self.assertRaises(ValueError):
            Card(rank = "Two",suit = "Diamonds")

    def test_incorrect_suit_name(self):
        with self.assertRaises(ValueError):
            Card(rank = "4", suit = "Dots")



