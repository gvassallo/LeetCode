# Given a binary tree, return the inorder traversal of its nodes' values.

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.helper(root, [])

    def helper(self, root, result):
        if root is None:
            return result
        self.helper(root.left, result)
        result.append(root.val)
        return self.helper(root.right, result)
