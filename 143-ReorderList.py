# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        self.helper(head, head)

    def helper(self, slow, fast):
        if fast.next is None:
            tmp = slow.next
            slow.next = None
            return tmp
        if fast.next.next is None:
            tmp = slow.next.next
            slow.next.next = None
            return tmp

        next = self.helper(slow.next, fast.next.next)
        tmp = next.next
        next.next = slow.next
        slow.next = next
        return tmp
