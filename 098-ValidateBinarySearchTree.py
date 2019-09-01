# Given a binary tree, determine if it is a valid binary search tree (BST).

import sys

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, -sys.maxsize, sys.maxsize)

    def validate(self, root, min_v, max_v):
        if root is None:
            return True
        if not min_v < root.val < max_v:
            return False
        left = self.validate(root.left, min_v, root.val)
        right = self.validate(root.right, root.val, max_v)
        return left and right
