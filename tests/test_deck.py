import unittest
from poker.card import Card
from poker.deck import Deck
class TestDeck(unittest.TestCase):
    def test_deck_initiated_with_no_cards(self):
        deck = Deck()
        self.assertEqual(deck.cards , [])
    def test_adds_cards_to_collection(self):
        card1 = Card(rank = "2",suit = "Diamonds")
        card2 = Card(rank = "3",suit = "Diamonds")
        deck = Deck()
        deck.add_cards([card1,card2])
        self.assertEqual(deck.cards, [card1,card2])

