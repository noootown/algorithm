# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# http://bit.ly/2IcaXN8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def __init__(self):
    self.prev = None

  def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if not root:
      return None
    self.flatten(root.right)
    self.flatten(root.left)

    root.right = self.prev
    root.left = None
    self.prev = root

class Solution:
  def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """

    def flat(root):
      if not root:
        return None
      l = flat(root.left)
      r = flat(root.right)

      root.left = None
      if not l:
        root.right = r
        return root
      else:
        root.right = l

      ptr = root.right
      if ptr:
        while ptr.right:
          ptr = ptr.right
        ptr.right = r

      return root

    flat(root)
