# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1: return [[1]]
        result = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        i = j = 0
        for z in range(n - 1):
            while j < n - z:
                result[i][j] = num
                num += 1
                j += 1
            j -= 1
            i += 1
            while i < n - z:
                result[i][j] = num
                num += 1
                i += 1
            i -= 1
            j -= 1
            while j >= z:
                result[i][j] = num
                num += 1
                j -= 1
            j += 1
            i -= 1
            while i > z:
                result[i][j] = num
                num += 1
                i -= 1
            i += 1
            j += 1
        return result
