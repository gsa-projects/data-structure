N = int(input("n: "))
board = [[0] * N for _ in range(N)]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end='')
            else:
                print(".", end='')
        print()
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
        elif N > col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        elif 0 <= col + (row - i) < N and board[i][col + (row - i)] == 1:
            return False
    return True

def is_safe_teacher(board, x, y):   # x <- col, y <- row
    for i in range(y):
        if board[i][x] == 1: return False
    for i, j in zip(range(y - 1, -1, -1), range(x - 1, -1, -1)):
        if board[i][j] == 1: return False
    for i, j in zip(range(y - 1, -1, -1), range(x + 1, N)):
        if board[i][j] == 1: return False
    return True

def solve(board, y):
    if y == N:
        print_board(board)
        return
    
    for j in range(N):
        # if is_safe(board, y, j):
        if is_safe_teacher(board, j, y):
            board[y][j] = 1
            solve(board, y + 1)
            board[y][j] = 0
            
solve(board, 0)