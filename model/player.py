from .hand import Hand

class Player:

    def __init__(self, name, chips=1000):
        self.name = name
        self.chips = chips
        self.hand = Hand()
        self.current_bet = 0

    def place_bet(self, amount):
        if amount > self.chips:
            raise ValueError("Bet exceeds available chips")
        
        if amount <= self.chips:
            self.current_bet = amount
            self.chips -= amount
            return True
        return False
    
    def normal_bet_win(self, multiplier=2):
        winnings = self.current_bet * multiplier
        self.chips += winnings

    def blackjack_bet_win(self, multiplier=2.5):
        winnings = int(self.current_bet * multiplier)
        self.chips += winnings

    def lose_bet(self):
        self.current_bet = 0

    def reset_hand(self):
        self.hand = Hand()

    def win_bet(self, multiplier=1):
        winnings = self.current_bet * (1 + multiplier)
        self.chips += winnings
        self.current_bet = 0

    def __str__(self):
        return f"{self.name}: Chips={self.chips}"



