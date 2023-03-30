import pygame
from pygame.locals import QUIT



pygame.init()

WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Conway Game of Life")

ROWS = 50
COLS = 50
CELL_SIZE = 20
MARGIN = 5

grid = []
for row in range(ROWS):
    grid.append([])
    for col in range(COLS):
        rect = pygame.Rect(col * (CELL_SIZE + MARGIN), row * (CELL_SIZE + MARGIN), CELL_SIZE, CELL_SIZE)
        grid[row].append(rect)

for row in range(ROWS):
    for col in range(COLS):
        pygame.draw.rect(screen, (255, 255, 255), grid[row][col])
        pygame.draw.rect(screen, (0, 0, 0), grid[row][col], 1)

pygame.display.update()


