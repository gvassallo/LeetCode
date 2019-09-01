# You are given a perfect binary tree where all leaves are on the same level, and every parent
# has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node,
# the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        self.helper(root.left, root.right)
        return root

    def helper(self, node1, node2):
        if node1 is None:
            return
        node1.next = node2
        self.helper(node1.left, node1.right)
        self.helper(node2.left, node2.right)
        self.helper(node1.right, node2.left)
