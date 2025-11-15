import random
from .card import Card

class Deck:

    def __init__(self):
        self.cards = []
        self.build_deck()
        self.shuffle()

    def build_deck(self):
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        return None
    
    def cards_remaining(self):
        return len(self.cards)
    
    