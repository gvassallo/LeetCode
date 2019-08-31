# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.helper([], 1, n, k, result)
        return result

    def helper(self, partial, curr, n, k, result):
        if len(partial) == k:
            return result.append(partial)
        for i in range(curr, n + 1):
            self.helper(partial + [i], i + 1, n, k, result)
