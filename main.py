from math import floor


class Cell:
    possibleValues = []

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
            block = floor(cellIndex / 3) % 3 + floor(cellIndex / 27) * 3
            row = floor(cellIndex / 9)
            col = cellIndex % 9
            # Create cell object
            cell = Cell(block, row, col, int(boardId[cellIndex]))
            # Add cell to lists
            self.cells.append(cell)
            self.blocks[block].append(cell)
            self.rows[row].append(cell)
            self.cols[col].append(cell)

    def updateCell(self, index, cell) -> None:
        boardCell = self.cells[index]
        boardCell = cell
        blockIndex = boardCell.row % 3 * 3 + boardCell.col % 3
        self.blocks[boardCell.block][blockIndex] = boardCell
        self.rows[boardCell.row][boardCell.col] = boardCell
        self.cols[boardCell.col][boardCell.row] = boardCell

    def checkIfFilled(self) -> bool:
        for cell in self.cells:
            if cell.value == 0:
                return False
        return True

    def getCode(self) -> str:
        code = ""
        for cell in self.cells:
            code += str(cell.value)
        return code


def findEmptyCell(cells, currentIndex) -> int:
    for index in range(currentIndex + 1, 81):
        if cells[index].value == 0:
            return index
    return -1


def getValue(board, index) -> int:
    possibleValues = [num for num in range(1, 10)]
    cell = board.cells[index]
    for i in range(9):
        block = board.blocks[cell.block][i]
        row = board.rows[cell.row][i]
        col = board.cols[cell.col][i]
        if block.value != 0 and block.value in possibleValues:
            possibleValues.remove(block.value)
        if row.value != 0 and row.value in possibleValues:
            possibleValues.remove(row.value)
        if col.value != 0 and col.value in possibleValues:
            possibleValues.remove(col.value)
    if len(possibleValues) == 1:
        return possibleValues[0], possibleValues
    else:
        return 0, possibleValues


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


def solve(boardId) -> str:
    board = Board(boardId)

    solved = False

    cellIndex = 0

    while solved == False:
        cellIndex = findEmptyCell(board.cells, cellIndex)
        if cellIndex != -1:
            cell = board.cells[cellIndex]
            cell.value, cell.possibleValues = getValue(board, cellIndex)
            board.updateCell(cellIndex, cell)
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
