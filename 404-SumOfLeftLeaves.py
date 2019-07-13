# Find the sum of all left leaves in a given binary tree.

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.helper(root, False)

    def helper(self, root, is_left):
        if root.left is None and root.right is None:
            if is_left:
                return root.val
            else:
                return 0
        res = 0
        if root.left:
            res += self.helper(root.left, True)
        if root.right:
            res += self.helper(root.right, False)
        return res
