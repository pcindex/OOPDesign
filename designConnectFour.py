import enum

class GridPosition(enum.Enum):
    EMPTY = 0,
    YELLOW = 1,
    RED = 2

class Grid:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = None
        self.initGrid()


    def initGrid(self):
        self._grid = ([[GridPosition.EMPTY for _ in range(self._columns)] 
                       for _ in range(self._rows_)]) #EMPTY for the size of columns *(copied) to the size of rows
        

    def getGrid(self):
        return self._grid
    

    def getColumnCount(self):  #shows which column is available to play the piece in
        return self._columns

    

    def placePiece(self, column, piece):
        if column < 0 or column >= self._columns:
            raise ValueError('Invalid column')
        if piece == GridPosition.EMPTY:
            raise ValueError('Invalid piece')
        
        for row in range(self._rows-1, -1, -1): # iteration starts at self.rows-1, stops at -1, and decrement by -1 for each iteration
            if self._grid[row][column] == GridPosition.EMPTY:
                self._grid[row][column] = piece
                return row
            



class Player:
    def __init__(self, name, pieceColor):
        self._name = name
        self._pieceColor = pieceColor


    def getName(self):
        return self._name
    

    def getPieceColor(self):
        return self._pieceColor
    


class Game:
    def __init__(self, grid, connectN, targetScore):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore

        self._players = [
            Player('Player 1', GridPosition.YELLOW),
            Player('Player 2', GridPosition.RED)
        ]

        self._score = {}
        for player in self._players:
            self._score[player.getName()] = 0


    def printBoard(self):
        print('Board:\n')
        grid = self._grid.getGrid()
        for i in range(len(grid)):
            row = ''
            for piece in grid[i]:
                if piece == GridPosition.EMPTY:
                    row += '0 '
                elif piece == GridPosition.YELLOW:
                    row += 'Y '
                elif piece == GridPosition.RED:
                    row += 'R '

            print(row)
        print('')


    def playMove(self, player):
        self.printBoard()
        print(f"{player.getName()}'s turn")
        colCnt = self._grid.getColumnCount()
        moveColumn = int(input(f"Enter column between {0} and {colCnt - 1} to add piece: "))
        moveRow = self._grid.placePiece(moveColumn, player.getPieceColor())
        return (moveRow, moveColumn)
    

    def playRound(self):
        while True:
            for player in self._players:
                row, col = self.playMove(player)
                pieceColor = player.getPieceColor()
                if self._grid.checkWin(self._connectN, row, col, pieceColor):
                    self._score[player.getName()] += 1
                    return player