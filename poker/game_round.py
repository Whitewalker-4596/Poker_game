class GameRound():
    def __init__(self,deck,players):
        self.deck = deck
        self.players = players
        self.community_rounds = {
            "flop" : 3,
            "river" : 1,
            "turn" : 1
        }
    def play(self):
        #shuffle the deck
        #give two cards to each player
        #ask fro wagers
        self._shuffle_cards()
        self._deal_initial_two_cards_to_each_player()
        self._make_bets()
        # self._deal_flop_cards()
        self._deal_community_cards(self.community_rounds["flop"])
        self._make_bets()
        self._deal_community_cards(self.community_rounds["river"])
        # self._deal_river_card()
        self._make_bets()
        self._deal_community_cards(self.community_rounds["turn"])
        # self._deal_turn_card()
        self._make_bets()


    def _shuffle_cards(self):
        self.deck.shuffle_cards()

    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards) 
        
    def _make_bets(self):
        for player in self.players:
            if player.wants_to_fold():
                self.players.remove(player)
                
    def _deal_community_cards(self,number_of_cards):
        community_cards = self.deck.remove_cards(number_of_cards)
        for player in self.players:
            player.add_cards(community_cards)

    # def _deal_flop_cards(self):
    #     flop_cards = self.deck.remove_cards(3)
    #     for player in self.players:
    #         player.add_cards(flop_cards)
            
    # def _deal_river_card(self):
    #     river_card = self.deck.remove_cards(1)
    #     for player in self.players:
    #         player.add_cards(river_card)

    # def _deal_turn_card(self):
    #     turn_card = self.deck.remove_cards(1)
    #     for player in self.players:
    #         player.add_cards(turn_card)


            