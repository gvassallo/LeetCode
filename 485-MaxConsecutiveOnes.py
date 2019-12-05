# Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0
        prev = 0

        for n in nums:
            if n == 1:
                if prev == 0:
                    cnt = 1
                else:
                    cnt += 1
            prev = n
            if cnt > max_cnt:
                max_cnt = cnt
        return max_cnt
