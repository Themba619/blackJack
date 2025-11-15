import pygame
import random

class MatrixEffect:

    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        
        #colors: fade to green shades
        self.BLACK = (0, 0, 0)
        self.GREEN_BRIGHT = (0, 255, 0)
        self.GREEN_MEDIUM = (0, 200, 0)
        self.GREEN_DIM = (0, 150, 0)
        self.GREEN_DARK = (0, 100, 0)
        
        self.FONT_SIZE = 13
        self.font = pygame.font.SysFont("Consolas", self.FONT_SIZE, bold=True)
        
        self.COLUMNS = self.width // self.FONT_SIZE
        
        self.drops = []
        for i in range(self.COLUMNS):
            self.drops.append({
                'y': random.randint(-20, 0),
                'speed': random.uniform(0.5, 2.0),
                'length': random.randint(8, 25)
            })

    def get_matrix_char(self):
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
        return random.choice(chars)

    def update(self):
        self.screen.fill(self.BLACK)

        for col in range(len(self.drops)):
            drop = self.drops[col]
            x = col * self.FONT_SIZE
            
            
            for trail_pos in range(drop['length']):
                char_y = (drop['y'] - trail_pos) * self.FONT_SIZE
                
                if 0 <= char_y <= self.height:
                    char = self.get_matrix_char()
                    
                    if trail_pos == 0:
                        color = self.GREEN_BRIGHT 
                    elif trail_pos < 3:
                        color = self.GREEN_MEDIUM
                    elif trail_pos < 6:
                        color = self.GREEN_DIM
                    else:
                        color = self.GREEN_DARK
                    
                    text = self.font.render(char, True, color)
                    self.screen.blit(text, (x, char_y))
            
            drop['y'] += drop['speed']
            
            
            if drop['y'] * self.FONT_SIZE > self.height + 100:
                drop['y'] = random.randint(-30, -5)
                drop['speed'] = random.uniform(0.5, 2.0)
                drop['length'] = random.randint(8, 25)