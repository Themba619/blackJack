class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def total_value(self):
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.is_ace())

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        
        return total
    
    def is_bust(self):
        return self.total_value() > 21
    
    def is_blackjack(self):
        return len(self.cards) == 2 and self.total_value() == 21
    
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
    