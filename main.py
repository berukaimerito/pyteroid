import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape


def main():
    game_over: bool= False
    updates = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    Shot.containers = (projectiles, drawables, updates)
    Asteroid.containers = (asteroids, drawables, updates)
    AsteroidField.containers = updates
    astro_field = AsteroidField()
    Player.containers = (updates, drawables)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while not game_over:
        screen.fill((0, 0, 0))
        delta_time = (clock.tick(60)) / 1000
        dt = delta_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        for obj in updates:
            obj.update(dt)
        for sprite in drawables:
            sprite.draw(screen)
        for ast in asteroids:
            if ast.collision_check(player1):
                game_over = True
                print("Game over looser")
            for bullet in projectiles:
                if bullet.colision_check(ast):
                    bullet.kill()
                    ast.kill()
        pygame.display.flip()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
