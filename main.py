import sys, pygame
from maze import Maze

cellSize = 50 #pixels
    
def drawCell(cell, screen):
    y = cell.y * cellSize
    x = cell.x * cellSize
    height =  cellSize
    width = cellSize
    color = (0, cell.visitorID, 0)
    #color = (100,(cell.y*cell.x*cellSize)%255,100)
    pygame.draw.rect(screen, color, [x, y, width, height])

def drawWalls(cell, screen):
    y = cell.y * cellSize
    x = cell.x * cellSize
    height =  cellSize
    width = cellSize
    color = (255,0,0)
    linesToDraw = []
    if cell.isWallAtMod(0,1): #Right
        linesToDraw.append([(x+(width), y+height), (x+width, y+height)])
    elif cell.isWallAtMod(0,-1): #Left
        linesToDraw.append([(x, y), (x, y+height)])
    elif cell.isWallAtMod(1,0): #Up
        linesToDraw.append([(x, y+height), (x+width, y+height)])
    elif cell.isWallAtMod(1,0): #Down
        linesToDraw.append([(x, y), (x+width, y)])
    for wall in linesToDraw:
        pygame.draw.line(screen, color, wall[0], wall[1], width=7)


def drawMaze(maze):
        #Setup
        screenSize = width, height = maze.WIDTH*cellSize, maze.HEIGHT*cellSize
        screen = pygame.display.set_mode(screenSize)
        
        #Draw Background
        black = (0,0,0)
        screen.fill(black)

        #Draw Cells
        for cell in maze.cells:
            drawCell(cell, screen)
        
        #Draw Walls
        for cell in maze.cells:
            drawWalls(cell, screen)

        #Display drawing
        pygame.display.flip()

def main():
    pygame.init()

    size = 5

    m = Maze(size, size)
    drawMaze(m)

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        if pygame.mouse.get_pressed()[0]:
            m = Maze(size, size)
            drawMaze(m)
        

if __name__ == "__main__":
    main()
