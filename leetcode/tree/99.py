# https://leetcode.com/problems/recover-binary-search-tree/description/
# http://bit.ly/2KzZDZr

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def recoverTree(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    res, stack, n1, n2 = None, [], None, None
    while True:
      while root:
        stack.append(root)
        root = root.left
      if len(stack) == 0:
        break
      node = stack.pop()
      if res and res.val > node.val:
        if not n1:
          n1 = res
        n2 = node
      res = node
      root = node.right
    n1.val, n2.val = n2.val, n1.val