import pygame
from utils.matrix_effect import MatrixEffect

class WelcomeScreen:

    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
    
        button_width = 200
        button_height = 100
        button_x = (self.screen_width - button_width) // 2
        button_y = (self.screen_height - button_height) // 2

        self.play_button = pygame.Rect(button_x, button_y, button_width, button_height)
        self.matrix = MatrixEffect(screen)
        self.font = pygame.font.SysFont("Consolas", 20, bold=True)
        self.button_text = self.font.render("Play BlackJack", True, (0, 0, 0))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.collidepoint(event.pos):
                    return "start_game"

        self.screen.fill((0, 0, 0))
        pygame.display.set_caption("Welcome to BlackJack")
        self.matrix.update()
        pygame.draw.rect(self.screen, (0, 255, 0), self.play_button)

        text_rect = self.button_text.get_rect(center=self.play_button.center)
        self.screen.blit(self.button_text, text_rect)

        return "continue"