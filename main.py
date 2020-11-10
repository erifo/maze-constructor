import sys, pygame
from maze import Maze

#Measurements in pixels.
MAZE_HEIGHT = 30
MAZE_WIDTH = 30
CELL_SIZE = 20
CELL_COLOR = (0,0,0)
WALL_WIDTH = 1
WALL_COLOR = (255,255,255)
    
def drawCell(maze, screen, originY, originX):
    for cell in maze.cells:
        y = originY + (cell.y * CELL_SIZE)
        x = originX + (cell.x * CELL_SIZE)
        height =  CELL_SIZE
        width = CELL_SIZE
        pygame.draw.rect(screen, CELL_COLOR, [x, y, width, height])

def drawWalls(maze, screen, originY, originX):
    for cell in maze.cells:
        y = originY + (cell.y * CELL_SIZE)
        x = originX + (cell.x * CELL_SIZE)
        height =  CELL_SIZE
        width = CELL_SIZE
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
            pygame.draw.line(screen, WALL_COLOR, line[0], line[1], width=WALL_WIDTH)

def drawVisitorID(maze, font, screen, originY, originX):
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 12)
    for cell in maze.cells:
        y = originY + (cell.y * CELL_SIZE)+10
        x = originX + (cell.x * CELL_SIZE)+10
        textSurface = font.render(str(cell.visitorID), False, (255, 255, 255))
        screen.blit(textSurface, (x, y))


def drawMaze(maze, screen, originY, originX):
        #Draw Background
        black = (0,0,0)
        screen.fill(black)
        drawCell(maze, screen, originY, originX)
        drawWalls(maze, screen, originY, originX)
        #drawVisitorID(maze, font, screen, originY, originX)
        pygame.display.flip()

def drawNewMaze(screen):
    maze = Maze(MAZE_HEIGHT, MAZE_WIDTH)
    drawMaze(maze, screen, 5, 5)

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

if __name__ == "__main__":
    main()
