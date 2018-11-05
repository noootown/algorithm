# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def rob(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
      return 0

    def dfs(root):
      if root.left is None and root.right is None:
        return root.val, 0
      lw, lwo = dfs(root.left) if root.left else (0, 0)
      rw, rwo = dfs(root.right) if root.right else (0, 0)
      return lwo + rwo + root.val, max(lw + rwo, rw + lwo, lw + rw, lwo + rwo)

    return max(*dfs(root))