# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        return self.helper(n, dp)

    def helper(self, n: int, dp: List[int]) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if dp[n] != 0:
            return dp[n]
        ways = self.helper(n - 1, dp)
        ways += self.helper(n - 2, dp)
        dp[n] = ways
        return ways
