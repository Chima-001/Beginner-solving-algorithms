def dfs_n_queens(n):
    if n < 1:
        return []
    results = []
    board = [-1] * n

    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if row - i == col - board[i]:
                return False
            if row - i == board[i] - col:
                return False

        return True

    def backtrack(board, row):
        if row == n:
            results.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack (board, row + 1)
                board[row] = -1
    backtrack(board, 0)
    return results

print(dfs_n_queens(1))
print(dfs_n_queens(2))
print(dfs_n_queens(4))
print(dfs_n_queens(5))