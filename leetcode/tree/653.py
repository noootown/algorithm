# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# http://bit.ly/2I8x9rA

class Solution:
  def findTarget(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """

    if not root:
      return False
    bfs, s = [root], set()
    for i in bfs:
      if k - i.val in s:
        return True
      s.add(i.val)
      if i.left:
        bfs.append(i.left)
      if i.right:
        bfs.append(i.right)
    return False