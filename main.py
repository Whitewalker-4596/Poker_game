from poker.card import Card
from poker.deck import Deck

deck = Deck()
cards = Card.create_standred_52_cards()
deck.add_cards(cards)

# card1 = Card("King","Hearts")
# card2 = Card("6","Diamonds")

# from main import deck ,cards