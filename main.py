from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player
from poker.game_round import GameRound
deck = Deck()
cards = Card.create_standred_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()
player1 = Player(name = "manu", hand = hand1)
player2 = Player(name = "bathukoli", hand = hand2)
players = [player1,player2]

game_round = GameRound(deck = deck, players = players)
game_round.play()
# card1 = Card("King","Hearts")
# card2 = Card("6","Diamonds")
# from main import deck ,cards, hand1, hand2, player1, player2, game_round

for player in players:
    print(f"{player.name} recieves a {player.hand}")
    index,hand_name,hand_cards = player.best_hand()
    hand_card_strings = [str(card) for card in hand_cards]
    hand_card_string = " and ".join(hand_card_strings)
    print(f"{player.name} has a {hand_name} with a {hand_card_string}")

winning_player = max(player1,player2)
print(f"the winning player is {winning_player}")

# print(player1.hand)
# print(player2.hand)
# print(player1.best_hand())
# print(player2.best_hand())


