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
    countx = 0
    counto = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if (board[i][j] == X):
                countx += 1
            elif (board[i][j] == O):
                counto += 1
    if countx > counto:
        return O
    else:
        return X


def actions(board):
    ans = set()

    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == EMPTY:
                ans.add((row, col))

    return ans


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    resultant = copy.deepcopy(board)
    resultant[action[0]][action[1]] = player(board)
    return resultant


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking each row
    if all(symbol == board[0][0] for symbol in board[0]):
        return board[0][0]
    elif all(symbol == board[1][0] for symbol in board[1]):
        return board[1][0]
    elif all(symbol == board[2][2] for symbol in board[2]):
        return board[2][0]
    # Check columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]
    # check diagnols
    if (board[1][1] == board[0][0] and board[2][2] == board[0][0]):
        return board[0][0]
    elif (board[0][2] == board[1][1] and board[2][0] == board[1][1]):
        return board[1][1]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None or (not any(EMPTY in subpart for subpart in board) and winner(board) is None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            v, movement = max_value(board)
            return movement
        else:
            v, movement = min_value(board)
            return movement


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    movement = None
    for action in actions(board):

        temp_v, act = min_value(result(board, action))
        if temp_v > v:
            v = temp_v
            movement = action
            if v == 1:
                return v, movement

    return v, movement


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    movement = None
    for action in actions(board):

        temp_v, act = max_value(result(board, action))
        if temp_v < v:
            v = temp_v
            movement = action
            if v == -1:
                return v, movement

    return v, movement
