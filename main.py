import pygame
from constants import *

GAME_OVER = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while not GAME_OVER: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_OVER = True
        screen.fill((0, 0, 0))
        pygame.display.flip()
        
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
