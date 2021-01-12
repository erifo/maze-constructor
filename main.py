import sys, pygame
from maze import Maze
from gfx import GFX
    
#Squares.
MAZE_HEIGHT = 15
MAZE_WIDTH = 15

#Pixels
ORIGIN_Y = 5
ORIGIN_X = 5

def showNewMaze():
    m = Maze(MAZE_HEIGHT, MAZE_WIDTH)
    gfx = GFX(m)
    gfx.drawMaze(ORIGIN_Y, ORIGIN_X)

def main():
    pygame.init()
    pygame.display.set_caption("Maze Constructor")
    
    showNewMaze()

    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                showNewMaze()

if __name__ == "__main__":
    main()
