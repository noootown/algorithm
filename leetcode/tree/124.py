# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.m = -100000

    def h(root):
      if not root:
        return 0
      rw, lw = h(root.right), h(root.left)
      rw = 0 if rw < 0 else rw
      lw = 0 if lw < 0 else lw
      nm = root.val + rw + lw
      self.m = self.m if nm < self.m else nm
      return root.val + max(rw, lw)

    h(root)
    return self.m
