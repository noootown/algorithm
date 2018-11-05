# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, left=False):
            if not root: return 0
            if left and root.left is root.right:
                return root.val
            return dfs(root.left, True) + dfs(root.right)
        return dfs(root)
