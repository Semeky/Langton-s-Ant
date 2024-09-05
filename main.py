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
while True:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    clock.tick(30)