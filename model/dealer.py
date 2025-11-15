from .hand import Hand

class Dealer:

    def __init__(self):
        self.hand = Hand()

    def reset_hand(self):
        self.hand = Hand()

    def should_hit(self):
        return self.hand.total_value() < 17
    
    def __str__(self):
        return f"Dealer's hand: {self.hand}"
    
    