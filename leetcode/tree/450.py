# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def deleteNode(self, root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    dummy = TreeNode(float('INF'))
    dummy.left = root
    self.replace(dummy, root, key)
    return dummy.left

  def replace(self, prev, cur, key):
    if not cur:
      return
    if cur.val < key:
      self.replace(cur, cur.right, key)
    elif cur.val > key:
      self.replace(cur, cur.left, key)
    else:
      if cur.left:
        left_right_most = cur.left
        while left_right_most.right:
          left_right_most = left_right_most.right
        left_right_most.right = cur.right

      if prev.val < key:
        prev.right = cur.left or cur.right
      else:
        prev.left = cur.left or cur.right