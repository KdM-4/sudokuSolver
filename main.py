import math


class Cell:
    def __init__(self, block, row, col, value, possibleValues):
        self.block = block
        self.row = row
        self.col = col
        self.value = value
        self.possibleValues = possibleValues


class Board:
    def __init__(self, board):
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
        print(i, row, col, block)
        board.append(Cell(block, row, col, code[i], []))
    return Board(board)


def display(code):
    """Prints out each row of the board with a | after the 3rd and 6th col, and a row of -'s after the 3rd and 6th row"""
    for row in range(9):
        rowString = ""
        for col in range(9):
            if col == 3 or col == 6:
                rowString += "| "
            rowString += code[col + row * 9] + " "
        if row == 3 or row == 6:
            print("-" * 21)
        print(rowString)


def solve(code):
    return


code = (
    "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
)

b = generateBoard(code)
# display(b.getCode())