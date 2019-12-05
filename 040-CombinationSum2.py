# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.
# Note:
#     All numbers (including target) will be positive integers.
#     The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtrack(0, sorted(candidates), target, [], result)
        return result

    def backtrack(self, current, candidates, target, partial, result):
        if current == target:
            return result.append(partial)
        if current > target or len(candidates) == 0:
            return

        self.backtrack(current + candidates[0], candidates[1:], target, partial + [candidates[0]], result)
        for i in range(1, len(candidates)):
            if candidates[i] != candidates[0]:
                self.backtrack(current, candidates[i:], target, partial, result)
                break
