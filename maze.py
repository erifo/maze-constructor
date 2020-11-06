from random import randint, choice

class Cell():
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.isVisited = False
        self.walls = self.initWalls()

    def initWalls(self):
        walls = {}
        directions = [-1, 0, 1]
        for yMod in directions:
            walls[yMod] = {}
            for xMod in directions:
                if (yMod == 0 and xMod == 0): #This is not a direction away from cell.
                    continue
                if (yMod != 0 and xMod != 0): #Diagonals are not valid directions.
                    continue
                walls[yMod][xMod] = True
        return walls
    
    def isWallAtMod(self, y, x):
        return self.walls[y][x]
    
    def razeWallAtMod(self, y, x):
        self.walls[y][x] = False

class Maze():
    def __init__(self, height, width):
        self.HEIGHT = height
        self.WIDTH = width
        self.cells = self.initCells()
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

    def linkCell(self, y, x):
        #Finding valid cell to link to.
        cell = self.getCellAt(y, x)
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        candidateCells = []
        for d in directions:
            #Ensure that there is a cell at coordinates.
            if (not self.isCellAt(y+d[0], x+d[1])):
                continue
            cell = self.getCellAt(y+d[0], x+d[1])
            #Ignore if candidate already links back into ours.
            if (not cell.isWallAtMod(d[0]*-1, d[1]*-1)):   
                continue
            candidateCells.append(cell)
        
        #End here if no more carvable cells are found.
        if (len(candidateCells) == 0):
            return

        #Link this cell to the found one.
        nextCell = choice(candidateCells)
        cell.razeWallAtMod(nextCell.y-y, nextCell.x-x)
        nextCell.razeWallAtMod((nextCell.y-y)*-1, (nextCell.x-x)*-1)
        self.linkCell(nextCell.y, nextCell.x)
         

        #Restarting process for next cell.
        self.linkCell(nextCell.y, nextCell.x)

    def linkMaze(self):
        startY = randint(0, self.HEIGHT-1)
        startX = randint(0, self.WIDTH-1)
        self.linkCell(startY, startX)

    def printMaze(self):
        payload = '╔' + '═'*self.WIDTH + '╗\n'
        for y in range(self.HEIGHT):
            payload += '║'
            for x in range(self.WIDTH):
                #cell = self.getCellAt(y, x)
                payload += ' #'
            payload += ' ║\n'
            if (y%2 == 0):
                payload += '║' + '#'*self.WIDTH + '║\n'
        payload += '╚' + '═'*self.WIDTH + '╝'
        print(payload)