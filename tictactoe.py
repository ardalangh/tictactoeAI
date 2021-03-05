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
    raise NotImplementedError


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
