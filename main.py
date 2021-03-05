import math


class Cell:
    def __init__(self, block, row, col, value, possibleValues) -> None:
        self.block = block
        self.row = row
        self.col = col
        self.value = value
        self.possibleValues = possibleValues


class Board:
    def __init__(self, board) -> None:
        self.list = board
        self.update()

    def update(self):
        """STUPID FUNCTION THAT DOES STUPID STUFF AAH"""
        # replace this garbage later
        # please
        # STUPID ASS IDEA!!!
        self.blocks = [[] for i in range(9)]
        self.rows = [[] for i in range(9)]
        self.cols = [[] for i in range(9)]
        for i in range(81):
            value = self.list[i].value
            block = math.floor(i / 3) % 3 + math.floor(i / 27) * 3
            row = math.floor(i / 9)
            col = i % 9
            self.blocks[block].append(value)
            self.rows[row].append(value)
            self.cols[col].append(value)

    def getCode(self) -> "code":
        """Returns the code of the current state of the board"""
        code = ""
        for cell in self.list:
            code += str(cell.value)
        return code


def generateBoard(code) -> Board:
    """Returns a Board object using a sudoku code"""
    board = []
    for i in range(81):
        block = math.floor(i / 3) % 3 + math.floor(i / 27) * 3
        row = math.floor(i / 9)
        col = i % 9
        # print(i, row, col, block)
        board.append(Cell(block, row, col, int(code[i]), []))
    return Board(board)


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


def findEmptyCell(cells, i):
    for cellI in range(i + 1, 81):
        if cells[cellI].value == 0:
            return cells.index(cells[cellI])
    return -1


def getPossibleValues(board, index):
    possibleValues = [i for i in range(1, 10)]
    cell = board.list[index]
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
    # print(possibleValues)
    return possibleValues


def solve(code) -> "code":
    board = generateBoard(code)
    cells = board.list

    drawBoard(board.getCode())

    i = 0

    solved = False
    tel = 0
    _max = 300
    while solved == False and tel < _max:
        emptyIndex = findEmptyCell(cells, i)
        if emptyIndex == i:
            i = 0
        else:
            i = emptyIndex
            if emptyIndex == -1:
                # solved = True
                solved = False
            cells[emptyIndex].possibleValues = getPossibleValues(board, emptyIndex)
            if len(cells[emptyIndex].possibleValues) == 1:
                cells[emptyIndex].value = cells[emptyIndex].possibleValues[0]
            board.update()
        tel += 1

    drawBoard(board.getCode())

    return board.getCode()


code = (
    "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
    # "100470000000162704060000000871045906300000051256090070027010508015680042603000100"
    # "000240003000000029706000000000000062100000000564000000400008790001004800090013000"
    # "600000300900470100700950000000390000030000002020000804006201000000000645408000000"
)

solve(code)
