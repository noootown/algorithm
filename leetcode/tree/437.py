# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

# 364 ms
class Solution:
  def helper(self, root, cache, target):
    if root:
      cache_ = defaultdict(int)
      for k, v in cache.items():
        cache_[k + root.val] = v
      cache_[root.val] += 1
      self.result += cache_[target]

      self.helper(root.left, cache_, target)
      self.helper(root.right, cache_, target)

  def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    self.result = 0
    self.helper(root, {}, sum)

    return self.result

# 64ms
class Solution(object):
    def helper(self, root, target, so_far, cache):
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far+root.val, 0)
            cache[so_far+root.val] += 1
            self.helper(root.left, target, so_far+root.val, cache)
            self.helper(root.right, target, so_far+root.val, cache)
            cache[so_far+root.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result