# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom
# right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1->3->1->1->1 minimizes the sum.


import sys 


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def helper(r, c):
            if r == m - 1 and c == n - 1: 
                return grid[r][c]
            if r >= m or c >= n: 
                return sys.maxsize
            if memo[r][c] == 0:
                memo[r][c] = grid[r][c]
                memo[r][c] += min(helper(r+1,c), helper(r, c+1))
            return memo[r][c]   
        
        m, n = len(grid), len(grid[0]) 
        memo = [[0] * n for _ in xrange(m)] 
        return helper(0, 0) 


if __name__ == "__main__": 
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    print Solution().minPathSum(grid)
