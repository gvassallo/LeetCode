# Given a linked list and a value x, partition it such that all nodes less than x come before
# nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode("dummy")
        dummy.next, head = head, dummy
        slow = head
        while slow.next and slow.next.val < x:
            slow = slow.next
        fast = slow.next
        while fast and fast.next:
            if fast.next.val < x:
                tmp = slow.next
                slow.next, fast.next = fast.next, fast.next.next
                slow.next.next, slow = tmp, slow.next
            else:
                fast = fast.next
        return head.next
