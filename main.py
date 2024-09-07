import pygame
from pygame.locals import *

pygame.init()

myfont = pygame.font.SysFont("monospace", 36)

black = (0, 0, 0)
white = (255, 255, 255)

steps = 0

width = 900
height = 900
cell_size = 10

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

COLS, ROWS = width // cell_size, height // cell_size
grid = [[0 for col in range(COLS)]for row in range(ROWS)]

rot = [(width//10)//2, (height//10)//2, 1]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
    screen.lock()
    for y_pos in range(ROWS):
        for x_pos in range(COLS):
            if grid[x_pos][y_pos] == 0:
                pygame.draw.rect(screen, (0, 0, 0), (x_pos*10, y_pos*10, cell_size, cell_size))
                grid[x_pos][y_pos] == 1
            else:
                pygame.draw.rect(screen, (255, 255, 255), (x_pos*10, y_pos*10, cell_size, cell_size))     

    if(grid[rot[1]][rot[0]] == 0):
        grid[rot[1]][rot[0]] = 1
        rot[2] = (rot[2] + 1) % 4
        if rot[2] == 0:
            rot[0] -= 1
        if rot[2] == 1:
            rot[1] += 1
        if rot[2] == 2:
            rot[0] += 1
        if rot[2] == 3:
            rot[1] -= 1
        steps += 1

    if(grid[rot[1]][rot[0]] == 1): 
        grid[rot[1]][rot[0]] = 0
        rot[2] = (rot[2] - 1) % 4
        if rot[2] == 0:
            rot[0] -= 1
        if rot[2] == 1:
            rot[1] += 1
        if rot[2] == 2:
            rot[0] += 1
        if rot[2] == 3:
            rot[1] -= 1 
        steps += 1

    strings = str(steps)
    steps_bar = myfont.render(strings, 1, (255,255,255))
  
    screen.unlock()
    screen.blit(steps_bar, (0,0))
    pygame.display.update()
    clock.tick(120)