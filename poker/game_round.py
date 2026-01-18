class GameRound():
    def __init__(self,deck,players):
        self.deck = deck
        self.players = players
    def play(self):
        #shuffle the deck
        #give two cards to each player
        #ask fro wagers
        self._shuffle_cards()
        self._deal_two_cards_to_each_player()

    def _shuffle_cards(self):
        self.deck.shuffle_cards()

    def _deal_two_cards_to_each_player(self):
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards) 

            