from constants import *
from asteroid import *
from player import *
import pygame
from asteroidfield import *
import sys
from shot import Shot

def main():

    #Starting Terminal Prompt
    print("\nStarting Asteroids!\n")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}\n\n")

    #Initializing aka Clusterfuck
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0 #frames

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for obj in asteroids:
            if obj.collison(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if obj.collison(bullet):
                    obj.split()
                    bullet.kill()

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60)/1000)


if __name__ == "__main__":
    main()
