# Given a linked list, swap every two adjacent nodes and return its head.
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Your algorithm should use only constant space. You may not modify the values in the
# list, only nodes itself can be changed.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None: 
            return head
        head = self.solution(head) 
        return head 
    
    def solution(self, head): 
        if head is None or head.next is None: 
            return head 
        next = head.next 
        nextnext = next.next 
        next.next = head 
        head.next = self.solution(nextnext) 
        return next 


