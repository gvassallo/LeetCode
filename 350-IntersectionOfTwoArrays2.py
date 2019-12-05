# Given two arrays, write a function to compute their intersection.
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_1 = {}
        for x in nums1:
            if x in freq_1:
                freq_1[x] += 1
            else:
                freq_1[x] = 1
        res = []
        for x in nums2:
            if x in freq_1 and freq_1[x] > 0:
                res.append(x)
                freq_1[x] -= 1
        return res
