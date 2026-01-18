import random
class Deck():
    def __init__(self):
        self.cards = []
        
    def __len__(self):
        return len(self.cards)

    def add_cards(self,cards):
        self.cards.extend(cards)

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def remove_cards(self,number):
        cards = self.cards[:number]
        del self.cards[:number]
        return cards