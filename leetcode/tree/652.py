# https://leetcode.com/problems/find-duplicate-subtrees/description/
# http://bit.ly/2JT4BiY
# very detailed
# http://bit.ly/2JV94RZ

from collections import defaultdict

# 112ms
class Solution:
  def findDuplicateSubtrees(self, root):
    """
    :type root: TreeNode
    :rtype: List[TreeNode]
    """
    def tuplify(root):
      if root:
        tuple = root.val, tuplify(root.left), tuplify(root.right)
        trees[tuple].append(root)
        return tuple

    trees = defaultdict(list)
    tuplify(root)
    return [roots[0] for roots in trees.values() if roots[1:]]

# 80ms
class Solution:
  def findDuplicateSubtrees(self, root):
    """
    :type root: TreeNode
    :rtype: List[TreeNode]
    """
    def getid(root):
      if root:
        # tuple as key
        id = treeid[root.val, getid(root.left), getid(root.right)]
        trees[id].append(root)
        return id

    trees = defaultdict(list)
    treeid = defaultdict()
    treeid.default_factory = treeid.__len__
    getid(root)
    return [roots[0] for roots in trees.values() if roots[1:]]