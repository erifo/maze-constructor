from random import randint, choice, shuffle

class Cell():
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.isVisited = False
        self.walls = self.initWalls()
        self.genID = 0

    def initWalls(self):
        walls = [(-1,0), (0,1), (1,0), (0,-1)]
        return walls
    
    def isWallAtMod(self, y, x):
        if ((y,x) in self.walls):
            return True
    
    def razeWallAtMod(self, y, x):
        if (not self.isWallAtMod(y, x)):
            print("ERROR: Wall", y, x, "in cell", self.y, x, "already razed!")
        else:
            self.walls = [wall for wall in self.walls if wall != (y,x)]

class Maze():
    def __init__(self, height, width):
        self.HEIGHT = height
        self.WIDTH = width
        self.cells = self.initCells()
        self.generationTracer = 1
        self.linkMaze()
    
    def initCells(self):
        cells = []
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                cells.append(Cell(y, x))        
        return cells

    def isCellAt(self, y, x):
        for cell in self.cells:
            if (cell.y == y and cell.x == x):
                return True
        return False

    def getCellAt(self, y, x):
        for cell in self.cells:
            if (cell.y == y and cell.x == x):
                return cell
        print("ERROR: Cell", y, x, "not found!")
    
    def getNeighbourCells(self, cell):
        payload = []
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        for d in directions:
            #Ensure that there is a cell at coordinates.
            if (not self.isCellAt(cell.y+d[0], cell.x+d[1])):
                continue
            c2 = self.getCellAt(cell.y+d[0], cell.x+d[1])
            payload.append(c2)
        return payload

    def linkCells(self, startY, startX):
        stack = []
        stack.append(self.getCellAt(startY, startX))
        while (len(stack) > 0):
            currentCell = stack.pop()
            currentCell.isVisited = True
            neighbourCells = self.getNeighbourCells(currentCell)
            candidateCells = [cell for cell in neighbourCells if not cell.isVisited]
            #---
            currentCell.genID = self.generationTracer
            self.generationTracer += 1
            #---
            if (len(candidateCells) == 0):
                continue
            #---
            stack.append(currentCell)
            nextCell = choice(candidateCells)
            currentCell.razeWallAtMod(nextCell.y - currentCell.y, nextCell.x - currentCell.x)
            nextCell.razeWallAtMod((nextCell.y - currentCell.y)*-1, (nextCell.x - currentCell.x)*-1)
            nextCell.isVisited = True
            stack.append(nextCell)

    def createOpenings(self):
        #Top
        y = 0
        x = randint(0, self.WIDTH-1)
        cell = self.getCellAt(y, x)
        cell.razeWallAtMod(-1,0)
        #Bottom
        y = self.HEIGHT-1
        x = randint(0, self.WIDTH-1)
        cell = self.getCellAt(y, x)
        cell.razeWallAtMod(1,0)

    def linkMaze(self):
        self.debugTracer = 0
        #startY = randint(0, self.HEIGHT-1)
        #startX = randint(0, self.WIDTH-1)
        startY = startX = 0
        self.linkCells(startY, startX)
        self.createOpenings()