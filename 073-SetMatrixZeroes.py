# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_has_zero = False
        column_has_zero = False

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                row_has_zero = True
                break

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                column_has_zero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                self.nullify_row(matrix, i)
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                self.nullify_col(matrix, j)

        if row_has_zero:
            self.nullify_row(matrix, 0)
        if column_has_zero:
            self.nullify_col(matrix, 0)
        return matrix

    def nullify_row(self, matrix: List[List[int]], row: int): -> None
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

    def nullify_col(self, matrix: List[List[int]], col: int): -> None
        for i in range(len(matrix)):
            matrix[i][col] = 0
