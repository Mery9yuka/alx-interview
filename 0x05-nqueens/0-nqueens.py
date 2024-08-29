#!/usr/bin/python3
# a program that solves the N queens problem.
import sys


def is_safe(board, row, col):
    """
    function that check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False

    return True


def solve_nqueens(board, row):
    """
    Function using backtracking to find all solutions for the N Queens problem
    """
    N = len(board)
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
