import pygame
from collections import deque

pygame.init()
width = 1600
height = 900
cell_size = 10
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
ROWS, COLS = width // cell_size, height // cell_size
grid = [[0 for col in range(COLS)]for row in range(ROWS)]
x_pos = ROWS
y_pos = COLS
value = grid[x_pos][y_pos]
grid[x_pos][y_pos] = not value
increments = deque([(1, 0), (0, 1), (-1, 0), (0, -1)])
size = cell_size
rect = x_pos * cell_size, y_pos * cell_size, size - 1, size - 1
if value:
    pygame.draw.rect(screen, (pygame.Color('white'), rect))
else:
    pygame.draw.rect(screen, (pygame.Color('black'), rect))
increments.rotate(1) if value else increments.rotate(-1)
dx, dy = increments[0]
x_pos = (x_pos + dx) % COLS
y_pos = (y_pos + dy) % ROWS
while True:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    value = grid[x_pos][y_pos]
    grid[x_pos][y_pos] = not value
    pygame.display.flip()
    clock.tick(30)