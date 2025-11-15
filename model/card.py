class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ["K", "Q", "J"]:
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)
        
    def is_ace(self):
        return self.rank == "A"
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"