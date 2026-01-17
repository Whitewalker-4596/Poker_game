import unittest
from unittest.mock import MagicMock
from poker.player import Player
from poker.hand import Hand
from poker.card import Card
class TestPlayer(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        player = Player(name = "manu",hand = hand)
        self.assertEqual(player.name ,"manu")
        self.assertEqual(player.hand , hand)

    def test_figuers_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player(name = "manu",hand = mock_hand)
        player.best_hand()
        self.assertEqual(
            player.best_hand(),
            "Straight Flush"
        )
        # mock_hand.best_rank.assert_called()
    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player1 = Player(name = "ravi",hand = mock_hand)
        cards = [
            Card("3","Hearts"),
            Card("King","Diamonds")
        ]
        player1.add_cards(cards = cards)
        mock_hand.add_cards.asssert_calls_once_with(cards)
