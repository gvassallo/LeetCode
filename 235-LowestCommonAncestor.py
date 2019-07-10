# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
# two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a
# node to be a descendant of itself).”

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        if p.val == root.val:
            return p
        if q.val == root.val:
            return q

        p_left = self.contains(root.left, p)
        q_left = self.contains(root.left, q)

        if p_left and q_left:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_left and not q_left:
            return root
        else:
            return self.lowestCommonAncestor(root.right, p, q)

    def contains(self, root, n):
        if root is None:
            return False
        if root.val == n.val:
            return True
        return self.contains(root.left, n) or self.contains(root.right, n)
