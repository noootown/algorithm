# https://leetcode.com/problems/subtree-of-another-tree/description/
# http://bit.ly/2JQywID

# 92ms
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

# 128ms
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

# 76ms
class Solution:
  def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    def dfs(s, t, on):
      if not s and not t:
        return True
      if not s or not t:
        return False
      if on and s.val != t.val:
        return False
      if s.val == t.val:
        if dfs(s.left, t.left, True) and dfs(s.right, t.right, True):
          return True
      return dfs(s.left, t, False) or dfs(s.right, t, False)

    return dfs(s, t, False)

