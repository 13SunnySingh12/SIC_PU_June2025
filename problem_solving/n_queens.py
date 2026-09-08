'''
N-Queens Problem:- 

Goal: 
-> Place n queens on an n x n chessboard such that no two queens attack each other.

Constraints:
1) No two queens in the same row
2) No two queens in the same column
3) No two queens on the same diagonal'''


def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
    # Check vertical column
    for i in range(row):
        if (board[i][col] == 'Q'):
            return False

    # Check upper-left diagonal
    i = row
    j = col
    while (i >= 0 and j >= 0):
        if (board[i][j] == 'Q'):
            return False
        i = i - 1
        j = j - 1

    # Check upper-right diagonal
    i = row
    j = col
    while (i >= 0 and j < n):
        if (board[i][j] == 'Q'):
            return False
        i = i - 1
        j = j + 1

    return True

def solve_n_queens(board, row, n):
    if (row == n):
        print_board(board)
        return
    else:
        for col in range(n):
            if (is_safe(board, row, col, n)):
                board[row][col] = 'Q'   # Place queen
                solve_n_queens(board, row + 1, n)
                board[row][col] = '.'   # Backtrack
            else:
                continue  # Not safe, try next column

def n_queens(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append('.')
        board.append(row)

    print("Solutions for", n, "-Queens Problem:\n")
    solve_n_queens(board, 0, n)



if __name__ == "__main__":
    N = int(input("Enter the value of N: "))
    if (N <= 0):
        print("N must be a positive integer greater than 0.")
    else:
        n_queens(N)
