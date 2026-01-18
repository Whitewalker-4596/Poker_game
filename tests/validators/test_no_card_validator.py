import unittest
from poker.card import Card
from poker.validators import NoCardValidator
class TestNOCardValidator(unittest.TestCase):
    def test_validates_there_are_no_cards(self):
        cards = []
        validator = NoCardValidator(cards)
        self.assertEqual(
        validator.is_valid(),
        True
        )