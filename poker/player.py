class Player():
    def __init__(self, name,hand):
        self.name = name
        self.hand = hand
    def __lt__(self,another_player):
        current_player_best_validator_index = self.best_hand()[0] 
        another_player_best_validator_index = another_player.best_hand()[0]
        return current_player_best_validator_index > another_player_best_validator_index
    def __str__(self):
        return self.name

    def best_hand(self):
        return self.hand.best_rank()
        
    def add_cards(self,cards):
        self.hand.add_cards(cards = cards)

    def wants_to_fold(self):
        return False