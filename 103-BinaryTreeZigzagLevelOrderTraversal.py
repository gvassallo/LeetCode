# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.helper(root, 0, result)
        return result

    def helper(self, root, level, result):
        if root is None:
            return
        if len(result) == level:
            result.append([root.val])
        elif level % 2 == 0:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)
