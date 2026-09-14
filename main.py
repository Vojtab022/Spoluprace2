import pygame
import sys

# Tyto soubory vytvoří tví kolegové v jiných větvích
from player import Player
from coin import Coin

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bezkolizní Git Hra")
    clock = pygame.time.Clock()

    hrac = Player(400, 300)
    mince = Coin()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30, 30, 30)) 

        hrac.move()
        
        mince.draw(screen)
        hrac.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()