# Remove all elements from a linked list of integers that have value val.

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        while head and head.val == val:
            head = head.next
        curr = head
        while curr and curr.next != None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
