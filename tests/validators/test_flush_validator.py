import unittest
from poker.validators import FlushValidator
from poker.card import Card
class TestFlushValidator(unittest.TestCase):
    def setUp(self):
        self.four_of_hearts = Card(rank = "4",suit = "Hearts")
        self.five_of_hearts = Card(rank = "5",suit = "Hearts")
        self.eight_of_hearts = Card(rank = "8",suit = "Hearts")
        self.jack_of_hearts = Card(rank = "Jack",suit = "Hearts")
        self.king_of_hearts = Card(rank = "King",suit = "Hearts")
        self.ace_of_hearts = Card(rank = "Ace",suit = "Hearts")
        self.cards = [
            Card(rank = "2", suit = "Spades"),
            self.four_of_hearts,
            self.five_of_hearts,
            self.eight_of_hearts,
            self.jack_of_hearts,
            self.king_of_hearts,
            self.ace_of_hearts
        ]
        # self.cards = [Card(rank = "2", suit = "Spades")] + [
        #     Card(rank = rank,suit = "Hearts")
        #     for rank in ["4","5","8","Jack","King","Ace"]
        # ]

    def test_validates_cards_has_fulsh(self):
        validator = FlushValidator(cards= self.cards)
        self.assertEqual(
            validator.is_valid(),
            True
            )
    
    def test_returns_flush_cards_from_card_collectiono(self):
        validator = FlushValidator(cards= self.cards)
        self.assertEqual(
            validator.best_cards(),
            [
            self.five_of_hearts,
            self.eight_of_hearts,
            self.jack_of_hearts,
            self.king_of_hearts,
            self.ace_of_hearts
            ]
        )
            # Card(rank = flush_rank,suit = "Hearts")
            # for flush_rank in ["5","8","Jack","king","Ace"]