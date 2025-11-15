import pygame
from game.blackjack_game import BlackjackGame, GameState
from utils.shuffle_effect import ShuffleEffect

class GameScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        self.game = BlackjackGame("Player")
        
        self.font = pygame.font.SysFont("Consolas", 24, bold=True)
        self.small_font = pygame.font.SysFont("Consolas", 18)
        
        self.hit_button = pygame.Rect(50, 500, 100, 50)
        self.stand_button = pygame.Rect(200, 500, 100, 50)
        self.deal_button = pygame.Rect(350, 500, 100, 50)
        self.bet_button = pygame.Rect(500, 500, 100, 50)
        
        self.shuffle_effect = None
        self.showing_shuffle = False
        
        self.bet_amount = 50
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return self.handle_click(event.pos)
            elif event.type == pygame.KEYDOWN:
                return self.handle_keypress(event.key)
        
        if self.showing_shuffle and self.shuffle_effect:
            if not self.shuffle_effect.update():
                self.showing_shuffle = False
                self.shuffle_effect = None
        
        self.draw()
        return "continue"
    
    def handle_click(self, pos):
        if self.showing_shuffle:
            return "continue"
            
        if self.game.can_hit() and self.hit_button.collidepoint(pos):
            self.game.hit()
        elif self.game.can_stand() and self.stand_button.collidepoint(pos):
            self.game.stand()
        elif self.game.can_bet() and self.bet_button.collidepoint(pos):
            if self.bet_amount > self.game.player.chips:
                return "continue"
            if self.game.place_bet(self.bet_amount):
                self.start_shuffle_animation()
        elif self.game.state == GameState.GAME_OVER and self.deal_button.collidepoint(pos):
            self.game.new_round()
            
        return "continue"
    
    def handle_keypress(self, key):
        if self.game.can_bet():
            if key == pygame.K_UP:
                self.bet_amount = min(self.bet_amount + 10, self.game.player.chips)
            elif key == pygame.K_DOWN:
                self.bet_amount = max(self.bet_amount - 10, self.game.minimum_bet)
        return "continue"
    
    def start_shuffle_animation(self):
        self.shuffle_effect = ShuffleEffect(self.screen)
        self.showing_shuffle = True
    
    def draw(self):
        self.screen.fill((0, 100, 0))
        
        if self.showing_shuffle:
            return
            
        self.draw_cards()
        self.draw_scores()
        self.draw_buttons()
        self.draw_game_info()
        
    def draw_cards(self):
        dealer_y = 50
        for i, card in enumerate(self.game.dealer.hand.cards):
            card_x = 50 + (i * 100)
            if i == 0 and self.game.state not in [GameState.GAME_OVER, GameState.DEALER_TURN]:
                self.draw_card_back(card_x, dealer_y)
            else:
                self.draw_card(card, card_x, dealer_y)
        
        player_y = 300
        for i, card in enumerate(self.game.player.hand.cards):
            card_x = 50 + (i * 100)
            self.draw_card(card, card_x, player_y)
    
    def draw_card(self, card, x, y):
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, 90, 120))
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 90, 120), 2)
        
        rank_text = self.font.render(card.rank, True, (0, 0, 0))
        suit_text = self.small_font.render(card.suit, True, (255, 0, 0) if card.suit in ['Hearts', 'Diamonds'] else (0, 0, 0))
        
        self.screen.blit(rank_text, (x + 8, y + 8))
        self.screen.blit(suit_text, (x + 8, y + 35))
    
    def draw_card_back(self, x, y):
        pygame.draw.rect(self.screen, (0, 0, 200), (x, y, 90, 120))
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 90, 120), 2)
    
    def draw_scores(self):
        if self.game.state in [GameState.GAME_OVER, GameState.DEALER_TURN]:
            dealer_score = self.game.dealer.hand.total_value()
        else:
            dealer_score = "?"
        dealer_text = self.font.render(f"Dealer: {dealer_score}", True, (255, 255, 255))
        self.screen.blit(dealer_text, (50, 20))
        
        player_score = self.game.player.hand.total_value()
        player_text = self.font.render(f"Player: {player_score}", True, (255, 255, 255))
        self.screen.blit(player_text, (50, 270))
    
    def draw_buttons(self):
        if self.game.can_hit():
            pygame.draw.rect(self.screen, (255, 255, 255), self.hit_button)
            hit_text = self.font.render("HIT", True, (0, 0, 0))
            self.screen.blit(hit_text, (self.hit_button.x + 25, self.hit_button.y + 15))
            
        if self.game.can_stand():
            pygame.draw.rect(self.screen, (255, 255, 255), self.stand_button)
            stand_text = self.font.render("STAND", True, (0, 0, 0))
            self.screen.blit(stand_text, (self.stand_button.x + 10, self.stand_button.y + 15))
            
        if self.game.can_bet():
            pygame.draw.rect(self.screen, (255, 255, 0), self.bet_button)
            bet_text = self.font.render("BET", True, (0, 0, 0))
            self.screen.blit(bet_text, (self.bet_button.x + 25, self.bet_button.y + 15))
            
        if self.game.state == GameState.GAME_OVER:
            pygame.draw.rect(self.screen, (0, 255, 0), self.deal_button)
            deal_text = self.font.render("DEAL", True, (0, 0, 0))
            self.screen.blit(deal_text, (self.deal_button.x + 20, self.deal_button.y + 15))
    
    def draw_game_info(self):
        chips_text = self.font.render(f"Chips: ${self.game.player.chips}", True, (255, 255, 255))
        self.screen.blit(chips_text, (500, 20))
        
        if self.game.can_bet():
            bet_text = self.font.render(f"Bet: ${self.bet_amount}", True, (255, 255, 255))
            self.screen.blit(bet_text, (500, 50))
            
            if self.bet_amount > self.game.player.chips:
                error_text = self.font.render("Not Enough Chips!", True, (255, 0, 0))
                self.screen.blit(error_text, (300, 450))
                
        elif self.game.player.current_bet > 0:
            bet_text = self.font.render(f"Current Bet: ${self.game.player.current_bet}", True, (255, 255, 255))
            self.screen.blit(bet_text, (500, 50))
        
        if self.game.player.chips < self.game.minimum_bet and self.game.can_bet():
            game_over_text = self.font.render("GAME OVER - No chips left!", True, (255, 0, 0))
            self.screen.blit(game_over_text, (250, 400))
        
        if self.game.result:
            result_text = self.font.render(str(self.game.result.value).replace('_', ' ').title(), True, (255, 255, 0))
            self.screen.blit(result_text, (300, 200))