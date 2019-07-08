# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
#     The number of elements initialized in nums1 and nums2 are m and n respectively.
#     You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[i] = nums1[m - 1]
                m -= 1
            else:
                nums1[i] = nums2[n - 1]
                n -= 1
            i -= 1
        while n > 0:
            nums1[i] = nums2[n - 1]
            n -= 1
            i -= 1
