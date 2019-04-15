"""
Game of Life 01/03/2019
"""
import pygame
import numpy as np
import random

grid_height = 50
grid_width = 50

cell_width = 10
cell_height = 10

window_height = grid_height * cell_height
window_width = grid_width * cell_width


grid = np.zeros((grid_height, grid_width))
grid_next = np.zeros((grid_height, grid_width))

# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

""" Select colors. """

live_color = green
dead_color = black

def cell(seed, n1, n2, n3, n4, n5, n6, n7, n8):
    ps = seed
    ns = 0
    neighbors = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
    if ps == 1:
        if (2 <= neighbors <= 3):
            ns = 1
        else:
            ns = 0
    if ps == 0:
        if neighbors == 3:
            ns = 1
        else:
            ns = 0

    return ns


""" Set up random grid """

probability = 60
isAlive = 0

for x in range(grid_height):
    for y in range(grid_width):
        randInt = random.randint(0,100)
        if randInt < probability:
            isAlive = 1
        else:
            isAlive = 0
        grid[x][y] = isAlive        
print(grid)        


def glider(x, y):
        grid[x][y]=1
        grid[x+1][y]=1
        grid[x+2][y]=1
        grid[x+2][y+1]=1
        grid[x+1][y+2]=1
"""
for x in range(grid_height-1):
    for y in range(grid_width-1):
        if x % 10 == 0:
            if y % 10 == 0:
                glider(x, y)

"""

pygame.init()

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Game Of Life')

clock = pygame.time.Clock()



game = True

while game:
    
    """ Check for quit. """
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game = False
    
    """ Display the current grid pattern. """
    for x in range(grid_height):
        for y in range(grid_width):
            if grid[x][y] == 1:
                pygame.draw.rect(gameDisplay, (live_color), [y * cell_width, x * cell_height, cell_width, cell_height], 1)
            else:
                pygame.draw.rect(gameDisplay, (dead_color), [y * cell_width, x * cell_height, cell_width, cell_height], 1)
    pygame.display.update()
    
    """ 
    Create next grid. 
    """
    
    """ Top left corner. """
    grid_next[0][0] = cell(
            
            grid[0][0], 
            grid[grid_height - 1][grid_width - 1],
            grid[grid_height - 1][0],
            grid[grid_height - 1][1],
            grid[0][1],
            grid[1][1],
            grid[1][0],
            grid[1][grid_width-1],
            grid[0][grid_width-1]

             )
    """ Top Right Corner """
    grid_next[0][grid_width-1] = cell(
            
            grid[0][grid_width-1],
            grid[grid_height-1][grid_width-2],
            grid[grid_height-1][grid_width-1],
            grid[grid_height-1][0],
            grid[0][0],
            grid[1][0],
            grid[1][grid_width-1],
            grid[1][grid_width-2],
            grid[0][grid_width-2])

    """ Bottom Right Corner """
    grid_next[grid_height-1][grid_width-1] = cell(

            grid[grid_height-1][grid_width-1],
            grid[grid_height-2][grid_width-2],
            grid[grid_height-2][grid_width-1],
            grid[grid_height-2][0],
            grid[grid_height-1][0],
            grid[0][0],
            grid[0][grid_width-1],
            grid[0][grid_width-2],
            grid[grid_height-1][grid_width-2])

    """ Bottom Left Corner """
    grid_next[grid_height-1][0] = cell(

            grid[grid_height-1][0],
            grid[grid_height-2][grid_width-1],
            grid[grid_height-2][0],
            grid[grid_height-2][1],
            grid[grid_height-1][1],
            grid[0][1],
            grid[0][0],
            grid[0][grid_width-1],
            grid[grid_height-1][grid_width-1])
    
    """ Left Edge """
    for x in range(1, grid_height-1):
        grid_next[x][0] = cell(

            grid[x][0],
            grid[x-1][grid_width-1],
            grid[x-1][0],
            grid[x-1][1],
            grid[x][1],
            grid[x+1][1],
            grid[x+1][0],
            grid[x+1][grid_width-1],
            grid[x][grid_width-1])

    """ Top Edge """
    for y in range(1, grid_width-1):
        grid_next[0][y] = cell(

            grid[0][y],
            grid[grid_height-1][y-1],
            grid[grid_height-1][y],
            grid[grid_height-1][y+1],
            grid[0][y+1],
            grid[1][y+1],
            grid[1][y],
            grid[1][y-1],
            grid[0][y-1])

    """ Right Edge """
    for x in range(1, grid_height-1):
        grid_next[x][grid_width-1] = cell(

            grid[x][grid_width-1],
            grid[x-1][grid_width-2],
            grid[x-1][grid_width-1],
            grid[x-1][0],
            grid[x][0],
            grid[x+1][0],
            grid[x+1][grid_width-1],
            grid[x+1][grid_width-2],
            grid[x][grid_width-2])

    """ Bottom Edge """
    for y in range(1, grid_width-1):
        grid_next[grid_height-1][y] = cell(

            grid[grid_height-1][y],
            grid[grid_height-2][y-1],
            grid[grid_height-2][y],
            grid[grid_height-2][y+1],
            grid[grid_height-1][y+1],
            grid[0][y+1],
            grid[0][y],
            grid[0][y-1],
            grid[grid_height-1][y-1])

    """ Inner Region """
    for i in range(1, grid_height-1):
        for j in range(1, grid_width-1):
            grid_next[i][j] = cell(

                grid[i][j],
                grid[i-1][j-1],
                grid[i-1][j],
                grid[i-1][j+1],
                grid[i][j+1],
                grid[i+1][j+1],
                grid[i+1][j],
                grid[i+1][j-1],
                grid[i][j-1])
            
    """ Update grid. """
    for a in range(grid_height):
        for b in range(grid_width):
            grid[a][b] = grid_next[a][b]  
            
            
pygame.quit()
quit()
