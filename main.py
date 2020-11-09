import sys, pygame
from maze import Maze

#Measurements in pixels.
MAZE_WIDTH = 32
MAZE_HEIGHT = 16
CELL_SIZE = 16
WALL_WIDTH = 2
    
def drawCell(cell, screen, originY, originX):
    y = originY + (cell.y * CELL_SIZE)
    x = originX + (cell.x * CELL_SIZE)
    height =  CELL_SIZE
    width = CELL_SIZE
    #color = (0, cell.visitorID, 0)
    color = (0,0,0)
    #color = (100,(cell.y*cell.x*CELL_SIZE)%255,100)
    pygame.draw.rect(screen, color, [x, y, width, height])

def drawWalls(cell, screen, originY, originX):
    y = originY + (cell.y * CELL_SIZE)
    x = originX + (cell.x * CELL_SIZE)
    height =  CELL_SIZE
    width = CELL_SIZE
    color = (255,255,255)
    linesToDraw = []
    if cell.isWallAtMod(0,1): #Right
        linesToDraw.append([(x+width, y), (x+width, y+height)])
    if cell.isWallAtMod(0,-1): #Left
        linesToDraw.append([(x, y), (x, y+height)])
    if cell.isWallAtMod(1,0): #Down
        linesToDraw.append([(x, y+height), (x+width, y+height)])
    if cell.isWallAtMod(-1,0): #Up
        linesToDraw.append([(x, y), (x+width, y)])
    for line in linesToDraw:
        pygame.draw.line(screen, color, line[0], line[1], width=WALL_WIDTH)


def drawMaze(maze, screen, originY, originX):
        #Draw Background
        black = (0,0,0)
        screen.fill(black)

        #Draw Cells
        for cell in maze.cells:
            drawCell(cell, screen, originY, originX)
        
        #Draw Walls
        for cell in maze.cells:
            drawWalls(cell, screen, originY, originX)

        #Display drawing
        pygame.display.flip()

def drawNewMaze(screen):
    m = Maze(MAZE_HEIGHT, MAZE_WIDTH)
    drawMaze(m, screen, 5, 5)

def main():
    #Setup
    pygame.init()
    pygame.display.set_caption("Maze Constructor")
    screenSize = (MAZE_WIDTH*CELL_SIZE)+10, (MAZE_HEIGHT*CELL_SIZE)+10 #tuple
    screen = pygame.display.set_mode(screenSize)
    
    drawNewMaze(screen)

    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                drawNewMaze(screen)

        #if pygame.mouse.get_pressed()[0]:
        

if __name__ == "__main__":
    main()
