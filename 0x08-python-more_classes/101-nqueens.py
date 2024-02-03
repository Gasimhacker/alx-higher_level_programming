#!/usr/bin/python3

"""This module solves the Nqueens puzzle
    and prints the solution in the following format:
    [[r, c], [r, c], [r, c], [r, c]]
    where r and c are indices that represent where a queen should
    be placed on the chessboard"""

import sys


def add_solution(board, res):
    """ Add the solution to the list of solutions

    Args:
        board (list): A matrix containing one of the Nqueens solutions
                      with the place of the queens set to 1
        res (list): The list of all Nqueen solutions
    """
    length = range(len(board))
    sol = [[i, j] for i in length for j in length if board[i][j] == 1]
    res.append(sol)


def solveNQ(n):
    """ Solve the Nqueens puzzle

    Args:
        n (int): The number of queens - The size of the chessboard

    Returns:
        A list containing all the possible solutions to the puzzle
    """
    col = set()
    pos_diag = set()
    neg_diag = set()

    res = []
    board = [[0] * n for i in range(n)]

    def backtrack(r):
        """ Solve the Nqueens puzzle using the backtracking technique

        Args:
            r (int): The row number
        """
        if r == n:
            add_solution(board, res)
            return
        for c in range(n):
            if (c in col or (r + c) in pos_diag or (r - c) in neg_diag):
                continue

            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = 1

            backtrack(r + 1)

            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = 0

    backtrack(0)
    return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    elif sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    elif int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solveNQ(int(sys.argv[1]))
    [print(sol) for sol in solutions]
