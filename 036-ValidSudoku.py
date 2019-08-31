# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                row_msg = "{} in row {}".format(num, i)
                col_msg = "{} in col {}".format(num, j)
                box_msg = "{} in box {}".format(num, (i // 3) * 3 + (j // 3))

                if row_msg in seen or col_msg in seen or box_msg in seen:
                    return False
                seen.add(row_msg)
                seen.add(col_msg)
                seen.add(box_msg)
        return True
