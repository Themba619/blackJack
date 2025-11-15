from enum import Enum
from model.deck import Deck
from model.player import Player
from model.dealer import Dealer


class GameState(Enum):
    BETTING = "betting"
    DEALING = "dealing"
    PLAYER_TURN = "player_turn"
    DEALER_TURN = "dealer_turn"
    GAME_OVER = "game_over"

class GameResult(Enum):
    PLAYER_WIN = "player_win"
    DEALER_WIN = "dealer_win"
    PUSH = "push"
    PLAYER_BLACKJACK = "player_blackjack"
    PLAYER_BUST = "player_bust"
    DEALER_BUST = "dealer_bust"

class BlackjackGame: 

    def __init__(self, player_name="Player"):
        self.player = Player(player_name)
        self.dealer = Dealer()
        self.deck = Deck()
        self.state = GameState.BETTING
        self.result = None
        self.minimum_bet = 10

    def place_bet(self, amount):
        if self.state != GameState.BETTING:
            return False

        if amount < self.minimum_bet:
            return False
        
        if self.player.place_bet(amount):
            self.deal_initial_cards()
            return True
        return False
    
    def deal_initial_cards(self):
        self.player.reset_hand()
        self.dealer.reset_hand()

        for _ in range(2):
            self.player.hand.add_card(self.deck.deal_card())
            self.dealer.hand.add_card(self.deck.deal_card())

        self.state = GameState.DEALING
        self.check_initial_blackjack()

    def check_initial_blackjack(self):
        player_blackjack = self.player.hand.is_blackjack()
        dealer_blackjack = self.dealer.hand.is_blackjack()

        if player_blackjack and dealer_blackjack:
            self.result = GameResult.PUSH
            self.state = GameState.GAME_OVER
        elif player_blackjack:
            self.result = GameResult.PLAYER_BLACKJACK
            self.state = GameState.GAME_OVER
        elif dealer_blackjack:
            self.result = GameResult.DEALER_WIN
            self.state = GameState.GAME_OVER
        else:
            self.state = GameState.PLAYER_TURN

    def hit(self):
        if self.state != GameState.PLAYER_TURN:
            return False
        
        self.player.hand.add_card(self.deck.deal_card())

        if self.player.hand.is_bust():
            self.result = GameResult.PLAYER_BUST
            self.state = GameState.GAME_OVER
            return True
        
        return True
    
    def stand(self):
        if self.state != GameState.PLAYER_TURN:
            return False
        
        self.state = GameState.DEALER_TURN
        self.dealer_play()
        return True
    
    def dealer_play(self):
        while self.dealer.should_hit():
            self.dealer.hand.add_card(self.deck.deal_card())

        self.determine_winner()
        self.state = GameState.GAME_OVER

    def determine_winner(self):
        player_total = self.player.hand.total_value()
        dealer_total = self.dealer.hand.total_value()

        if self.dealer.hand.is_bust():
            self.result = GameResult.DEALER_BUST
        elif dealer_total > player_total:
            self.result = GameResult.DEALER_WIN
        elif player_total > dealer_total:
            self.result = GameResult.PLAYER_WIN
        else:
            self.result = GameResult.PUSH

    def payout(self):
        if self.result == GameResult.PLAYER_BLACKJACK:
            self.player.win_bet(1.5)
        elif self.result in [GameResult.PLAYER_WIN, GameResult.DEALER_BUST]:
            self.player.win_bet(1.0)
        elif self.result == GameResult.PUSH:
            self.player.chips += self.player.current_bet
            self.player.current_bet = 0
        else:
            self.player.lose_bet()

    def new_round(self):
        self.payout()
        self.result = None
        self.state = GameState.BETTING

        if self.deck.cards_remaining() < 15:
            self.deck = Deck()

    def can_hit(self):
        return self.state == GameState.PLAYER_TURN

    def can_stand(self):
        return self.state == GameState.PLAYER_TURN

    def can_bet(self):
        return self.state == GameState.BETTING