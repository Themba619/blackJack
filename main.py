import pygame
from screens.welcome_screen import WelcomeScreen
from screens.game_screen import GameScreen

#pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
current_screen = WelcomeScreen(screen)
game_screen = None

while running:
    result = current_screen.update()

    if result == "quit":
        running = False
    elif result == "start_game":
        game_screen = GameScreen(screen)
        current_screen = game_screen

    pygame.display.flip()
    clock.tick(60)

pygame.quit()