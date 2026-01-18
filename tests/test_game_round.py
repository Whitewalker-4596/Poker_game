import unittest
from unittest.mock import MagicMock,call
from poker.game_round import GameRound
from poker.card import Card
# from poker.player import Player
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
        
    def test_deals_2_initial_cards_from_deck_to_each_player(self):
        first_two_cards = [
            Card("3","Hearts"),
            Card("6","Clubs")
        ]
        next_two_cards = [
            Card("4","Spades"),
            Card("Ace","Diamonds")
        ]
        mock_deck = MagicMock()
        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        mock_deck.remove_cards.side_effect = [first_two_cards,next_two_cards]
        
        mock_players = [
            mock_player1,mock_player2
        ]
        game_round = GameRound(deck = mock_deck, players = mock_players)
        game_round.play()
        mock_deck.remove_cards.assert_has_calls(
            [call(2),call(2)]
        )
        #the below tests when add_cards is called on player 
        #the remove cards is invoked on deck and 
        #player is getting the same 2 cards that are returned
        #from deck objects return value (sideeffect = varies return value )

        mock_player1.add_cards.assert_called_once_with(first_two_cards)
        mock_player2.add_cards.assert_called_once_with(next_two_cards)


