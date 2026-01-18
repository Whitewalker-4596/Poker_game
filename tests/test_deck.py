import unittest
from unittest.mock import patch
from poker.card import Card
from poker.deck import Deck
class TestDeck(unittest.TestCase):
    def test_deck_initiated_with_no_cards(self):
        deck = Deck()
        self.assertEqual(deck.cards , [])
    def test_len_function_on_deck_gives_no_of_cards_in_deck(self):
        deck = Deck()
        self.assertEqual(len(deck),0)
        cards = [
            Card(rank = "2",suit = "Diamonds"),
            Card(rank = "3",suit = "Clubs")
        ]
        deck.add_cards(cards)
        self.assertEqual(len(deck),2)
    def test_adds_cards_to_collection(self):
        card1 = Card(rank = "2",suit = "Diamonds")
        card2 = Card(rank = "3",suit = "Diamonds")
        deck = Deck()
        deck.add_cards([card1,card2])
        self.assertEqual(deck.cards, [card1,card2])
    @patch('random.shuffle')
    def test_gameplay_shuffels_the_deck(self,mock_shuffle):
        cards = [
            Card(rank = "2",suit = "Diamonds"),
            Card(rank = "3",suit = "Clubs")
        ]
        deck = Deck()
        deck.add_cards(cards = cards)
        deck.shuffle_cards()
        mock_shuffle.assert_called_once_with(cards)

    def test_removes_n_number_of_cards(self):

        ace = Card(rank = "Ace",suit = "Diamonds"),
        king = Card(rank = "King",suit = "Clubs")
        cards = [ace,king]
        deck = Deck()
        deck.add_cards(cards = cards)
        self.assertEqual(deck.remove_cards(1),[ace])
        self.assertEqual(deck.cards,[king])

