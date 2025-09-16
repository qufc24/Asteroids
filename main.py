from constants import *
from player import *
import pygame


def main():

    #Starting Terminal Prompt
    print("\nStarting Asteroids!\n")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}\n\n")

    #Initializing
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0 #frames

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()

        dt = (clock.tick(60)/1000)


if __name__ == "__main__":
    main()
