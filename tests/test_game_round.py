import unittest
from unittest.mock import MagicMock,call
from poker.game_round import GameRound
from poker.card import Card
from poker.hand import Hand
# from poker.player import Player
class TestGameRound(unittest.TestCase):
    def setUp(self):
        self.first_two_cards = [
            Card("3","Hearts"),
            Card("6","Clubs")
        ]
        self.next_two_cards = [
            Card("4","Spades"),
            Card("Ace","Diamonds")
        ]
        self.flop_cards = [
            Card("King","Spades"),
            Card("8","Diamonds"),
            Card("2","Diamonds")
        ]
        self.river_card = [
            Card("7", "Spades")
        ]
        self.turn_card = [
            Card("10", "Hearts")
        ]

        self.mock_deck = MagicMock()
        self.mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.river_card,
            self.turn_card
        ]

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
        mock_deck.shuffle_cards.assert_called_once()

    def test_deals_2_initial_cards_from_deck_to_each_player(self):
        
        mock_deck = self.mock_deck
        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
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
        #assert_called_once_with checks the last call made on the function
        mock_player1.add_cards.assert_has_calls([
            call(self.first_two_cards)
            ])
        mock_player2.add_cards.assert_has_calls([
            call(self.next_two_cards)
            ])

    def test_removes_player_if_not_willing_to_bet(self):
        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        players = [mock_player1,mock_player2]
        mock_deck = MagicMock()
        game_round = GameRound(deck = mock_deck,players = players)
        mock_player1.wants_to_fold.return_value = False
        mock_player2.wants_to_fold.return_value = True
        game_round.play()

        mock_player2.wants_to_fold.assert_called_once()
        self.assertEqual(game_round.players,[mock_player1])

    def test_deals_same_3_flop_cards_1_river_1_turn_card(self):
        mock_player1 = MagicMock()
        mock_player1.wants_to_fold.return_value = False
        mock_player2 = MagicMock()
        mock_player2.wants_to_fold.return_value = False
        players = [mock_player1,mock_player2]

        mock_deck = self.mock_deck

        game_round = GameRound(deck = mock_deck,players=players)
        game_round.play()

        mock_deck.remove_cards.assert_has_calls([
            call(3),call(1),call(1)
            ])

        calls = [
            call(self.flop_cards),
            call(self.river_card),
            call(self.turn_card)
        ]
        for player in game_round.players:
            player.add_cards.assert_has_calls(calls)

            
        






