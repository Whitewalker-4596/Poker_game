class NoCardValidator():
    def __init__(self,cards):
        self.cards = cards
        self.name = "No Cards"
    def is_valid(self):
        return len(self.cards) == 0