import random

obs1 = [[0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [2, 0, 1, 0],
        [2, 0, 0, 0]]

obs2 = [[0, 0, 0, 2],
        [0, 1, 0, 2],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]

obs3 = [[0, 0, 0, 0, 0, 2, 2],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [2, 2, 0, 0, 0, 0, 0]]

obs4 = [[2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 2]]

obs5 = [[0, 0, 0, 2],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]]

obs6 = [[0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [2, 0, 0, 0]]

obs7 = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]]

obs8 = [[0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]]

obs9 = [[0, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]]

obstacles = [obs1, obs2, obs3, obs4, obs5, obs6, obs7, obs8, obs9]


def makeEmptyBoard(n):
    board = []
    for i in range(n):
        board.append([2] * n)

    return board


def isLegalChange(board, obs, i, j):
    rows = len(obs)
    cols = len(obs[0])
    if (i + rows > len(board)) or (j + cols > len(board)):
        return False
    for row in range(rows):
        for col in range(cols):
            if board[i + row][j + col] != 2:
                return False
    return True


def makeChange(board, obs, i, j):
    rows = len(obs)
    cols = len(obs[0])
    for row in range(rows):
        for col in range(cols):
            board[i + row][j + col] = obs[row][col]


def change2s(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0


def makeBoard(n, shapes):
    board = makeEmptyBoard(n)
    for i in range(n):
        for j in range(n):
            if ((i > 3) or (j > 3)) and ((i < n - 7) or (j < n - 6)):
                obs = random.choice(shapes)
                if isLegalChange(board, obs, i, j):
                    makeChange(board, obs, i, j)
    change2s(board, n)
    return board