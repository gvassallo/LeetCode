# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left
# to right, level by level).

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.helper(root, 0, result)
        return result

    def helper(self, root, level, result):
        if root is None:
            return
        if len(result) == level:
            result.append([])
        result[level].append(root.val)
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)
