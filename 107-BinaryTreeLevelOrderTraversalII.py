# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        return self.helper(root, 0, [])[::-1]

    def helper(self, root: TreeNode, level: int, result: List[List[int]]) -> List[List[int]]:
        if root is None:
            return []
        if len(result) == level:
            result.append([])
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)
        result[level].append(root.val)
        return result
