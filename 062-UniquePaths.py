# A robot is located at the top-left corner of a m x n grid. 
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid.
#
# How many possible unique paths are there?


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def helper(r, c): 
            if r >= m or c >= n: 
                return 0 
            if r == m - 1 and c == n - 1: 
                return 1 
            if paths[r][c] == 0: 
                paths[r][c] = helper(r + 1, c) 
                paths[r][c] += helper(r, c + 1) 
            return paths[r][c]
        
        paths = [[0] * n for _ in xrange(m)] 
        return helper(0, 0) 


if __name__ == "__main__":
    print Solution().uniquePaths(1, 2)

