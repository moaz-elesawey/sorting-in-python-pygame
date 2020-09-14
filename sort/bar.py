import pygame
import random
from .constants import BAR_WIDTH, HEIGHT, BAR_COLOR

class Bar:
    def __init__(self, x, y, color=BAR_COLOR, width=BAR_WIDTH):
        self.x = x
        self.width = width
        self.height = random.randrange(0, HEIGHT-10)
        self.color = color
        # self.y = HEIGHT - self.height
        self.y = y

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.width, self.height])
    
    def __repr__(self):
        return f"Bar({self.height})"

    def __lt__(self, other):
        return self.height < other.height
