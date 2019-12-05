# Given an n-ary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        return self.helper(root, 0, [])

    def helper(self, node, level, result):
        if node is None:
            return result
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        for c in node.children:
            self.helper(c, level + 1, result)
        return result
