import math


def getPositions(board):
    values, index, row, col, block = [], [], [], [], []
    for i in range(81):
        cell = board[math.floor(i / 9)][i % 9]
        values.append(cell)
        index.append(i + 1)
        block.append((math.floor(i / 3) % 3 + math.floor(i / 27) * 3) + 1)
        row.append((math.floor(i / 9)) + 1)
        col.append((i % 9) + 1)
    return [values, index, row, col, block]


lists = getPositions(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)