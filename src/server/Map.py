import numpy as np
import ships

ROT90 = np.array([[0, -1], [1, 0]])

class Board:
    def __init__(self, gridSize: np.array):
        self.gridSize = gridSize
        self.ships = []
        self.grid = [[None for i in range(gridSize[0])] for i in range(gridSize[1])]
    
    def addShip(self, ship: ships.Ship) -> int:
        for coord in ship.getCoords():
            if self.indexGrid(coord) != None:
                raise ValueError("Cannot place a ship in an occupied position")
        self.ships.append(ship)
        for coord in ship.getCoords():
            self.updateGrid(coord, len(self.ships) - 1)
        return len(self.ships) - 1

    def indexGrid(self, x: int, y: int) -> int:
        return self.grid[x][y]
    
    def indexGrid(self, pos: np.array) -> int:
        return self.grid[pos[0]][pos[1]]
    
    def updateGrid(self, pos: np.array, val: int):
        self.grid[pos[0]][pos[1]] = val

    def moveShip(self, index: int, dist: int):
        if self.ships[index].isDead():
            raise ValueError("Cannot move a dead ship")
        shipFacing = self.ships[index].facing
        coords = self.ships[index].getCoords()
        for i in range(len(coords)):
            coord = coords[i] + shipFacing * dist
            if coord[0] >= self.gridSize[0] or coord[1] >= self.gridSize[1]:
                raise ValueError("Cannot move a ship beyond the bounds of the board")
            val = self.indexGrid(coord)
            if val != None and val != index:
                raise ValueError("Cannot move ship into a position which contains another ship.")
        self.ships[index].step(dist)
        for i in range(len(coords)):
            self.updateGrid(coords[1], None)
        for coord in self.ships[index].getCoords():
            self.updateGrid(coord, index)
    
    def rotateShip(self, index: int, times: int):
        if self.ships[index].isDead():
            raise ValueError("Cannot rotate a dead ship")
        shipCentre = self.ships[index].getCentre()
        coords = self.ships[index].getCoords()
        for i in range(times):
            for x in range(len(coords)):
                coords[x] = np.matmul(ROT90, (coords[x] - shipCentre)) + shipCentre
        for coord in coords:
            if coord[0] >= self.gridSize[0] or coord[1] >= self.gridSize[1]:
                raise ValueError("Cannot rotate this ship as it would be over the edge of the board.")
        for coord in coords:
            val = self.indexGrid(coord)
            if val != None and val != index:
                raise ValueError("Cannot rotate this ship as it would be overlapping another ship.")
        for coord in self.ships[index].getCoords():
            self.updateGrid(coord, None)
        self.ships[index].rotate(times)
        for coord in coords:
            self.updateGrid(coord, index)
        
    def shoot(self, coord):
        ind = self.indexGrid(coord)
        if ind != None:
            ships[ind].hit(coord)
            if ships[ind].isDead():
                for c in ships[ind].getCoords():
                    self.updateGrid(c, None)
            return (True, ind, ships[ind].isDead())
        return False

class Game:
    def __init__(self):
        self.board = Board(np.array([30, 30]))
        self.p1Ships = []
        self.p2Ships = []
        self.p1Ships.append(self.board.addShip(ships.AirCarrier(np.array([4, 28]), np.array([1, 0]), 1)))
        self.p1Ships.append(self.board.addShip(ships.Battleship(np.array([3, 26]), np.array([1, 0]), 1)))
        self.p1Ships.append(self.board.addShip(ships.Cruiser(np.array([2, 24]), np.array([1, 0]), 1)))
        self.p1Ships.append(self.board.addShip(ships.Submarine(np.array([2, 22]), np.array([1, 0]), 1)))
        self.p1Ships.append(self.board.addShip(ships.Destroyer(np.array([1, 20]), np.array([1, 0]), 1)))
        self.p2Ships.append(self.board.addShip(ships.AirCarrier(np.array([25, 28]), np.array([-1, 0]), 2)))
        self.p2Ships.append(self.board.addShip(ships.Battleship(np.array([26, 26]), np.array([-1, 0]), 2)))
        self.p2Ships.append(self.board.addShip(ships.Cruiser(np.array([27, 24]), np.array([-1, 0]), 2)))
        self.p2Ships.append(self.board.addShip(ships.Submarine(np.array([27, 22]), np.array([-1, 0]), 2)))
        self.p2Ships.append(self.board.addShip(ships.Destroyer(np.array([28, 20]), np.array([-1, 0]), 2)))
    def addShip(self, ship: ships.Ship) -> int:
        return self.board.addShip(ship)
    def moveShip(self, index: int, dist: int):
        self.board.moveShip(index, dist)
    def rotateShip(self, index: int, times: int):
        self.board.rotateShip(index, times)
    def shoot(self, coord):
        self.board.shoot(coord)