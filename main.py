import pygame
from pygame.locals import *

pygame.init()

n = 0.1
auto = False
formiga = []
inte = 0
formiga.append(50)
formiga.append(50)
formiga.append(1)
playtime = 0.0

black = (0, 0, 0)
white = (255, 255, 255)


width = 1200
height = 1200
cell_size = 10

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

COLS, ROWS = width // cell_size, height // cell_size
grid = [[0 for col in range(COLS)]for row in range(ROWS)]

x_pos = COLS // 2
y_pos = ROWS // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    milliseconds = clock.tick(60)
    seconds = milliseconds / 1000.0
    playtime += milliseconds /1000.0
 
    screen.lock()
    for y_pos in range(COLS):
        for x_pos in range(ROWS):
            if grid[x_pos][y_pos] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (x_pos*10, y_pos*10, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, (0, 0, 0), (x_pos*10, y_pos*10, cell_size, cell_size))     

    if(grid[formiga[1]][formiga[0]] == 0 and playtime>=0.01):
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
        pygame.draw.rect(screen, (92,0,92), ((formiga[1]*cell_size,formiga[0]*cell_size), (cell_size,cell_size)))
        playtime = 0.0
        inte+=1
    if(grid[formiga[1]][formiga[0]] == 1 and playtime>=0.01): 
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
        pygame.draw.rect(screen, (92,0,92), ((formiga[1]*cell_size,formiga[0]*cell_size), (cell_size,cell_size))) 
        playtime = 0.0
        inte+=1
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)