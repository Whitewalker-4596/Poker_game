import unittest
from unittest.mock import MagicMock
from poker.game_round import GameRound
class TestGameRound(unittest.TestCase):
    def test_stores_deck_and_players(self):
        mock_deck = MagicMock()
        mock_players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(deck = mock_deck, players = mock_players)

        self.assertEqual(game_round.deck,mock_deck)
        self.assertEqual(game_round.players,mock_players)

    def test_gameplay_shuffels_the_deck(self):
        mock_deck = MagicMock()
        mock_players = [
            MagicMock(),
            MagicMock()
        ]
        game_round = GameRound(deck = mock_deck, players = mock_players)
        game_round.play()
        mock_deck.shuffle.assert_called_once()