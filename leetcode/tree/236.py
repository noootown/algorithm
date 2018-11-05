# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    def isParent(p, c):
      return p is not None and (p == c or isParent(p.left, c) or isParent(p.right, c))

    if root in (None, p, q):
      return root
    elif isParent(p, q):
      return p
    elif isParent(q, p):
      return q
    while root:
      if isParent(root.left, p) and isParent(root.left, q):
        root = root.left
      elif isParent(root.right, p) and isParent(root.right, q):
        root = root.right
      else:
        return root
    return root

class Solution:
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    def find(root, p):
      if not root:
        return False
      else:
        return root == p or find(root.left, p) or find(root.right, p)

    if find(p, q):
      return p
    elif find(q, p):
      return q
    else:
      pOnLeft = find(root.left, p)
      qOnLeft = find(root.left, q)
      if pOnLeft and qOnLeft:
        return self.lowestCommonAncestor(root.left, p, q)
      elif not pOnLeft and not qOnLeft:
        return self.lowestCommonAncestor(root.right, p, q)
      else:
        return root
