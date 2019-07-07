# You are given two non-empty linked lists representing two non-negative integers. The
# digits are stored in reverse order and each of their nodes contain a single digit. Add
# the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0
# itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0) 
        curr = head 
        carry = 0 
        while l1 or l2:
            curr.next = ListNode((l1.val + l2.val + carry) % 10)  
            carry = (l1.val + l2.val + carry) / 10
            curr, l1, l2 = curr.next, l1.next, l2.next 
        if l1: 
            while l1: 
                curr.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) / 10  
                curr, l1 = curr.next, l1.next 
        elif l2: 
            while l2: 
                curr.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) / 10
                curr, l2 = curr.next, l2.next 
        if carry: 
            curr.next = ListNode(1) 
        return head.next
