# https://leetcode.com/problems/subtree-of-another-tree/description/
# http://bit.ly/2JQywID

class Solution:
  def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    def convert(p):
      return '^%s#%s%s' % (str(p.val), convert(p.left), convert(p.right))

    return convert(t) in convert(s)

from hashlib import sha256
class Solution:
  def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    def hash_(x):
      S = sha256()
      S.update(x.encode("utf-8"))
      return S.hexdigest()

    def merkle(node):
      if not node:
        return '#'
      node.merkle = hash_(merkle(node.left) + str(node.val) + merkle(node.right))
      return node.merkle

    merkle(s)
    merkle(t)

    def dfs(node):
      if not node:
        return False
      return (node.merkle == t.merkle or dfs(node.left) or dfs(node.right))

    return dfs(s)
