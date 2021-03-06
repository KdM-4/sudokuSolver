import math


class Cell:
    def __init__(self, block, row, col, value) -> None:
        self.block = block
        self.row = row
        self.col = col
        self.value = value


class Board:
    cells = []
    blocks = [[] for i in range(9)]
    rows = [[] for i in range(9)]
    cols = [[] for i in range(9)]

    def __init__(self, boardId) -> None:
        for cellIndex in range(81):
            # Get corresponding indexes for positional lists
            block = math.floor(cellIndex / 3) % 3 + math.floor(cellIndex / 27) * 3
            row = math.floor(cellIndex / 9)
            col = cellIndex % 9
            # Create cell object
            cell = Cell(block, row, col, int(boardId[cellIndex]))
            # Add cell to lists
            self.cells.append(cell)
            self.blocks[block].append(cell.value)
            self.rows[row].append(cell.value)
            self.cols[col].append(cell.value)

    def updateCellValue(self, index, value) -> None:
        cell = self.cells[index]
        cell.value = value
        blockIndex = cell.row % 3 * 3 + cell.col % 3
        self.blocks[cell.block][blockIndex] = value
        self.rows[cell.row][cell.col] = value
        self.cols[cell.col][cell.row] = value

    def checkIfFilled(self):
        for cell in self.cells:
            if cell.value == 0:
                return False
        return True

    def getCode(self):
        code = ""
        for cell in self.cells:
            code += str(cell.value)
        return code


def findEmptyCell(cells, currentIndex):
    for index in range(currentIndex + 1, 81):
        if cells[index].value == 0:
            return index
    return -1


def getValue(board, index):
    possibleValues = [num for num in range(1, 10)]
    cell = board.cells[index]
    for i in range(9):
        blockVal = board.blocks[cell.block][i]
        rowVal = board.rows[cell.row][i]
        colVal = board.cols[cell.col][i]
        if blockVal != 0 and blockVal in possibleValues:
            possibleValues.remove(blockVal)
        if rowVal != 0 and rowVal in possibleValues:
            possibleValues.remove(rowVal)
        if colVal != 0 and colVal in possibleValues:
            possibleValues.remove(colVal)
    if len(possibleValues) == 1:
        return possibleValues[0]
    else:
        return 0


def createSeperator(start, mid, end) -> str:
    """Returns a seperator that is used by the drawBoard function"""
    return start + "─" * 7 + mid + "─" * 7 + mid + "─" * 7 + end


def drawBoard(code) -> None:
    """Draws the sudoku board to the screen"""
    rowList = []
    rowList.append(createSeperator("┌", "┬", "┐"))
    for x in range(9):
        if x == 3 or x == 6:
            rowList.append(createSeperator("├", "┼", "┤"))
        row = code[x * 9 : x * 9 + 9]
        rowString = "│ "
        for x in range(9):
            if x == 3 or x == 6:
                rowString += "│ "
            rowString += row[x] + " "
        rowString += "│"
        rowList.append(rowString)
    rowList.append(createSeperator("└", "┴", "┘"))
    for rowString in rowList:
        print(rowString)


def solve(boardId):
    board = Board(boardId)

    solved = False

    cellIndex = 0

    while solved == False:
        cellIndex = findEmptyCell(board.cells, cellIndex)
        if cellIndex != -1:
            cellValue = getValue(board, cellIndex)
            board.updateCellValue(cellIndex, cellValue)
        elif board.checkIfFilled():
            solved = True
        else:
            cellIndex = 0

    return board.getCode()


boardId = (
    "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
)

drawBoard(boardId)
solvedId = solve(boardId)
drawBoard(solvedId)
