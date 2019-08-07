# Given a Binary Search Tree and a target number, return true if there exist two
# elements in the BST such that their sum is equal to the given target.

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        return self.helper(root, k, set())

    def helper(self, root, k, nums):
        if not root:
            return False
        if k - root.val in nums:
            return True
        if root.val not in nums:
            nums.add(root.val)
        return self.helper(root.left, k, nums) or self.helper(root.right, k, nums)
