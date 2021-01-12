import sys, pygame

#Pixels
CELL_SIZE = 20
WALL_WIDTH = 1

#RGB
CELL_COLOR = (0,0,0)
WALL_COLOR = (255,255,255)

class GFX():
    def __init__(self, maze):
        self.maze = maze
        self.screenSize = (self.maze.WIDTH*CELL_SIZE)+10, (self.maze.HEIGHT*CELL_SIZE)+10 #tuple
        self.screen = pygame.display.set_mode(self.screenSize)
    
    def drawCell(self, originY, originX):
        for cell in self.maze.cells:
            y = originY + (cell.y * CELL_SIZE)
            x = originX + (cell.x * CELL_SIZE)
            height =  CELL_SIZE
            width = CELL_SIZE
            pygame.draw.rect(self.screen, CELL_COLOR, [x, y, width, height])

    def drawWalls(self, originY, originX):
        for cell in self.maze.cells:
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
                pygame.draw.line(self.screen, WALL_COLOR, line[0], line[1], width=WALL_WIDTH)

    def drawVisitorID(self, font, originY, originX):
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 12)
        for cell in self.maze.cells:
            y = originY + (cell.y * CELL_SIZE)+10
            x = originX + (cell.x * CELL_SIZE)+10
            textSurface = font.render(str(cell.visitorID), False, (255, 255, 255))
            self.screen.blit(textSurface, (x, y))


    def drawMaze(self, originY, originX):
            #Draw Background
            black = (0,0,0)
            self.screen.fill(black)
            self.drawCell(originY, originX)
            self.drawWalls(originY, originX)
            #drawVisitorID(font, originY, originX)
            pygame.display.flip()