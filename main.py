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
        self.board = board

    def getCode(self) -> "code":
        """Returns the code of the current state of the board"""
        code = ""
        for cell in self.board:
            code += cell.value
        return code


def generateBoard(code) -> Board:
    """Returns a Board object using a sudoku code"""
    board = []
    for i in range(81):
        block = math.floor(i / 3) % 3 + math.floor(i / 27) * 3
        row = math.floor(i / 9)
        col = i % 9
        # print(i, row, col, block)
        board.append(Cell(block, row, col, code[i], []))
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


def solve(code) -> "code":
    return


code = (
    "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
)

b = generateBoard(code)
drawBoard(b.getCode())
