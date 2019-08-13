# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            pre = pre.next
        curr = pre.next
        prev = None
        for _ in range(n - m + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        pre.next.next = curr
        pre.next = prev
        return dummy.next
