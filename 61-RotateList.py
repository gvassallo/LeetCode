# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# Example:
#
# Given 1->2->3->4->5->NULL and k = 2,
#
# return 4->5->1->2->3->NULL.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None: 
            return head 
        dummy = ListNode(0) 
        dummy.next = head 
        fast = dummy
        slow = dummy 
        i = 0 
        while fast.next:
            i += 1 
            fast = fast.next 
        for j in reversed(range(i - k % i)): 
            slow = slow.next
        fast.next = dummy.next 
        dummy.next  = slow.next 
        slow.next = None 
        return dummy.next 
