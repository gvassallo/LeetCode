# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Note: You have to rotate the image in-place, which means you have to modify the input 2D
# matrix directly. DO NOT allocate another 2D matrix and do the rotation.


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__": 
    matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
            ]
    Solution().rotate(matrix) 
    print matrix 
