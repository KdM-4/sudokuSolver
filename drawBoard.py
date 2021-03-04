def getString(row) -> str:
    rowString = "│ "
    for x in range(9):
        if x == 3 or x == 6:
            rowString += "│ "
        rowString += row[x] + " "
    rowString += "│"
    return rowString


def createSeperator(start, mid, end):
    return start + "─" * 7 + mid + "─" * 7 + mid + "─" * 7 + end


def drawBoard(board) -> None:
    rowList = []
    rowList.append(createSeperator("┌", "┬", "┐"))
    for x in range(9):
        if x == 3 or x == 6:
            rowList.append(createSeperator("├", "┼", "┤"))
        row = board[x * 9 : x * 9 + 9]
        rowList.append(getString(row))
    rowList.append(createSeperator("└", "┴", "┘"))
    for rowString in rowList:
        print(rowString)


board = (
    "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
)
drawBoard(board)
