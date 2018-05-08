# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# http://bit.ly/2FJSTVn

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
      return []

    stack = [root]
    res = []
    while stack:
      root = stack.pop()
      res.append(root.val)
      if root.left:
        stack.append(root.left)
      if root.right:
        stack.append(root.right)
    return res[::-1]

class Solution:
  def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []

    def pt(root):
      if root is None:
        return
      pt(root.left)
      pt(root.right)
      res.append(root.val)

    pt(root)
    return res