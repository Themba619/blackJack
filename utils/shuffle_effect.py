import pygame
import random

class ShuffleEffect:
    def __init__(self, screen):
        self.screen = screen
        self.timer = 60 
        self.cards = []
        
        for i in range(10):
            self.cards.append({
                'x': random.randint(100, 600),
                'y': random.randint(100, 400),
                'velocity_x': random.uniform(-5, 5),
                'velocity_y': random.uniform(-5, 5),
                'rotation': random.uniform(0, 360)
            })
    
    def update(self):
        self.timer -= 1
        
        for card in self.cards:
            card['x'] += card['velocity_x']
            card['y'] += card['velocity_y']
            card['rotation'] += 5
            
            if card['x'] < 0 or card['x'] > 750:
                card['velocity_x'] *= -1
            if card['y'] < 0 or card['y'] > 550:
                card['velocity_y'] *= -1
        
        self.draw()
        return self.timer > 0
    
    def draw(self):
        self.screen.fill((0, 100, 0))
        
        font = pygame.font.SysFont("Consolas", 48, bold=True)
        text = font.render("SHUFFLING...", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 300))
        self.screen.blit(text, text_rect)
        
        for card in self.cards:
            pygame.draw.rect(self.screen, (255, 255, 255), (card['x'], card['y'], 40, 60))
            pygame.draw.rect(self.screen, (0, 0, 0), (card['x'], card['y'], 40, 60), 2)