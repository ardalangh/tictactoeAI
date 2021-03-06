"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Ocount = 0 
    Xcount = 0 
    for row in board:
        Ocount += row.count(O)
        Xcount += row.count(X)
    if Xcount == Ocount: return O
    else: X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allPossibleActions = set()
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == EMPTY:
                allPossibleActions.add((i, j))
    return allPossibleActions





def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCpy = copy.deepcopy(board)
    boardCpy[action[0]][action[1]] = player(board)
    return boardCpy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # checks if any of the rows have a winner
    for j in range(3):
        if any(i == board[j][0] for i in board[0]): 
            return board[j][0]
    # check the cols
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
