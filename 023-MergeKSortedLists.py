# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for l in lists:
            curr = l
            while curr is not None:
                heappush(heap, curr.val)
                curr = curr.next

        head = tail = None
        while len(heap) > 0:
            num = heappop(heap)
            if head is None:
                head = tail = ListNode(num)
            else:
                tail.next = ListNode(num)
                tail = tail.next
        return head
