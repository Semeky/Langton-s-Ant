import pygame
from pygame.locals import *

pygame.init()

myfont = pygame.font.SysFont("monospace", 36)
formiga = []
inte = 0
formiga.append(45)
formiga.append(45)
formiga.append(1)

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

x_pos = 1
y_pos = 1

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

    if(grid[formiga[1]][formiga[0]] == 0):
        grid[formiga[1]][formiga[0]] = 1
        formiga[2] = (formiga[2] + 1) % 4
        if formiga[2] == 0:
            formiga[0] -= 1
        if formiga[2] == 1:
            formiga[1] += 1
        if formiga[2] == 2:
            formiga[0] += 1
        if formiga[2] == 3:
            formiga[1] -= 1
        steps += 1

    if(grid[formiga[1]][formiga[0]] == 1): 
        grid[formiga[1]][formiga[0]] = 0
        formiga[2] = (formiga[2] - 1) % 4
        if formiga[2] == 0:
            formiga[0] -= 1
        if formiga[2] == 1:
            formiga[1] += 1
        if formiga[2] == 2:
            formiga[0] += 1
        if formiga[2] == 3:
            formiga[1] -= 1 
        steps += 1

    strings = str(steps)
    label = myfont.render(strings, 1, (255,255,255))
  
    screen.unlock()
    screen.blit(label, (0,0))
    pygame.display.update()
    clock.tick(120)