from random import randint, choice

class Cell():
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.isVisited = False
        self.walls = self.initWalls()
        self.visitorID = 0

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
        self.linkMaze()
        self.debugTracer = 0
    
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

    def linkCell(self, y, x):
        #Finding valid cell to link to.
        currentCell = self.getCellAt(y, x)
        currentCell.isVisited = True
        candidateCells = self.getNeighbourCells(currentCell)

        #Disqualify already visited.
        candidateCells = [cell for cell in candidateCells if not cell.isVisited]
        
        #End here if no more linkable cells are found.
        if (len(candidateCells) == 0):
            return

        #Link this cell to the found one by razing inbetween walls.
        nextCell = choice(candidateCells)
        currentCell.razeWallAtMod(nextCell.y-y, nextCell.x-x)
        nextCell.razeWallAtMod((nextCell.y-y)*-1, (nextCell.x-x)*-1)

        #Marking the cell with number indicating when it was visited.
        currentCell.visitorID = self.debugTracer * max(1,(255 // (self.WIDTH*self.HEIGHT)))
        self.debugTracer += 1

        #Restarting process for next cell, twice.
        #This will cause depth-first branching paths to generate.
        self.linkCell(nextCell.y, nextCell.x)
        self.linkCell(nextCell.y, nextCell.x)

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
        startY = randint(0, self.HEIGHT-1)
        startX = randint(0, self.WIDTH-1)
        self.linkCell(startY, startX)
        self.createOpenings()