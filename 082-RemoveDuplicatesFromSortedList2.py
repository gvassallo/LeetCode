# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only
# distinct numbers from the original list.


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None: return head
        curr = head
        next = head.next
        prev = None
        while next:
            if curr.val == next.val:
                while next and curr.val == next.val:
                    next = next.next
                if next is None:
                    if prev is None:
                        return None
                    prev.next = None
                    break
                curr.val = next.val
                curr.next = next.next
                next = next.next
            else:
                prev = curr
                curr = next
                next = next.next
        return head
