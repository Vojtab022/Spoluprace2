import pygame
import random
 
class Coin:
    def __init__(self):
        # Náhodná pozice na obrazovce (800x600)
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)
        self.radius = 15
        self.color = (255, 215, 0) # Zlatá barva
 
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)