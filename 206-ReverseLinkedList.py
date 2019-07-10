# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        nex = head.next
        curr = head
        head.next = None

        while nex is not None:
            tmp = nex.next
            nex.next = curr
            curr = nex
            nex  = tmp

        return curr
