# Given an m x n grid of characters board and a string word,
# return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# he same letter cell may not be used more than once.

def exist(board: list, word: str) -> bool:
    # Big O(n * m * dfs)
    
    row, col = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True

        if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[i] or (r, c) in path:
            return False
        path.add((r, c))
        res = dfs(r+1, c, i+1) or dfs(r, c+1, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1)
        path.remove((r, c))
        return res

    for r in range(row):
        for c in range(col):
            if dfs(r, c, 0):
                return True
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))   # Output: true

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print(exist(board, word))   # Output: true

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board, word))   # Output: false
