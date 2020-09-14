import pygame
from .bar import Bar
from .constants import BAR_COUNT, BAR_WIDTH, WHITE, WIDTH, GREY, HEIGHT, RED


class Board:
    # bars = []
    def __init__(self):
        self.bars = []

    def draw_bars(self):
        for i in range(0, WIDTH, BAR_WIDTH):
            bar = Bar(i, 0)
            self.bars.append(bar)

    def draw_lines(self, win):
        for i in range(0, WIDTH, BAR_WIDTH):
            pygame.draw.line(win, GREY, (i, 0), (i, HEIGHT), 1)

    def draw(self, win):
        win.fill(WHITE)
        self.draw_lines(win)
        self.draw_bars()

    def make_grid(self, win):
        self.draw(win)

        # self.bars[-1].color = RED

        return self.bars

        