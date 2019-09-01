# Find the kth largest element in an unsorted array. Note that it is the kth largest element
# in the sorted order, not the kth distinct element.

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                if n > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, n)
        return min_heap[0]
