import math


def getPositions(board):
    """Returns matrices for blocks, rows and colums calculated from list or string of 81 positions"""
    blocks = [[] for i in range(9)]
    rows = [[] for i in range(9)]
    cols = [[] for i in range(9)]
    for i in range(81):
        cell = board[i]
        blocks[math.floor(i / 3) % 3 + math.floor(i / 27) * 3].append(cell)
        rows[math.floor(i / 9)].append(cell)
        cols[i % 9].append(cell)
    return blocks, rows, cols
