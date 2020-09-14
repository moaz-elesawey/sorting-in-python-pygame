import pygame 
from sort.constants import WIDTH, HEIGHT, WHITE
from sort.board import Board
from sort import qSort, bubbleSort, mergeSort
import time
from pprint import pprint

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algos")
board = Board()

def main():
    run = True
    clock = pygame.time.Clock()
    
    def draw(win, bars):
        
        win.fill(WHITE)
        for bar in bars:
            bar.draw(win)
        board.draw_lines(win)
        pygame.display.update()
        # time.sleep(10/1000)

    bars = board.make_grid(WIN)

    while run:

        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        draw(WIN, bars)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
 
            if keys[pygame.K_q]:
                qSort.q_sort(bars, 0, len(bars)-1, WIN, draw)
                draw(WIN, bars)

            if keys[pygame.K_b]:
                bubbleSort.bubble_sort(bars, len(bars)-1, WIN, draw)
                draw(WIN, bars)

            if keys[pygame.K_m]:
                mergeSort.merge_sort(bars, WIN, draw)
                draw(WIN, bars)

            if keys[pygame.K_SPACE]:
                qSort.q_sort(bars, 0, len(bars)-1, WIN, draw)
                draw(WIN, bars)
                
            if keys[pygame.K_r]:
                bars.clear()
                bars = board.make_grid(WIN)
                draw(WIN, bars)

        pygame.display.update()

if __name__ == '__main__':
    main()
