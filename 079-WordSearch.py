# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.helper(board, word, i, j):
                    return True
        return False

    def helper(self, board, word, row, col):
        if len(word) == 0:
            return True
        if not (0 <= row < len(board)) or not (0 <= col < len(board[row])):
            return False
        if board[row][col] != word[0]:
            return False

        board[row][col] = "FOO"
        moves = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        for m in moves:
            if self.helper(board, word[1:], row + m[0], col + m[1]):
                return True
        board[row][col] = word[0]
        return False
