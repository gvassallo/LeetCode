# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        result = []
        if not root.left and not root.right:
            return [str(root.val)]
        if root.left:
            for res in self.binaryTreePaths(root.left):
                result.append(str(root.val) + "->" + res)
        if root.right:
            for res in self.binaryTreePaths(root.right):
                result.append(str(root.val) + "->" + res)
        return result
