# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/solution/
# http://bit.ly/2FdBVhV
import sys

# answer 1
# class Solution(object):
#   def findNumberOfLIS(self, nums):
#     N = len(nums)
#     if N <= 1: return N
#     lengths = [0] * N  # lengths[i] = longest ending in nums[i]
#     counts = [1] * N  # count[i] = number of longest ending in nums[i]
#
#     for j, num in enumerate(nums):
#       for i in range(j):
#         if nums[i] < nums[j]:
#           if lengths[i] >= lengths[j]:
#             lengths[j] = 1 + lengths[i]
#             counts[j] = counts[i]
#           elif lengths[i] + 1 == lengths[j]:
#             counts[j] += counts[i]
#
#     longest = max(lengths)
#     return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

# answer 2
# class Node(object):
#   def __init__(self, start, end):
#     self.range_left, self.range_right = start, end
#     self._left = self._right = None
#     self.val = 0, 1  # length, count
#
#   @property
#   def range_mid(self):
#     return (self.range_left + self.range_right) // 2
#
#   @property
#   def left(self):
#     self._left = self._left or Node(self.range_left, self.range_mid)
#     return self._left
#
#   @property
#   def right(self):
#     self._right = self._right or Node(self.range_mid + 1, self.range_right)
#     return self._right
#
#
# def merge(v1, v2):
#   if v1[0] == v2[0]:
#     if v1[0] == 0: return (0, 1)
#     return v1[0], v1[1] + v2[1]
#   return max(v1, v2)
#
#
# def insert(node, key, val):
#   if node.range_left == node.range_right:
#     node.val = merge(val, node.val)
#     return
#   if key <= node.range_mid:
#     insert(node.left, key, val)
#   else:
#     insert(node.right, key, val)
#   node.val = merge(node.left.val, node.right.val)
#
#
# def query(node, key):
#   if node.range_right <= key:
#     return node.val
#   elif node.range_left > key:
#     return 0, 1
#   else:
#     return merge(query(node.left, key), query(node.right, key))
#
#
# class Solution(object):
#   def findNumberOfLIS(self, nums):
#     if not nums: return 0
#     root = Node(min(nums), max(nums))
#     for num in nums:
#       length, count = query(root, num - 1)
#       insert(root, num, (length + 1, count))
#     return root.val[1]

# answer 3
def bs(arr, val, key=lambda x: x):
  l, r = 0, len(arr) - 1
  if key(arr[l]) > val:
    return l
  if key(arr[r]) <= val:
    return r + 1
  while l + 1 < r:
    m = (l + r) >> 1
    v = key(arr[m])
    if v <= val:
      l = m
    else:
      r = m
  return r

def bs_left(arr, val, key=lambda x: x):
  l, r = 0, len(arr) - 1
  if key(arr[l]) >= val:
    return l
  if key(arr[r]) < val:
    return r + 1
  while l + 1 < r:
    m = (l + r) >> 1
    v = key(arr[m])
    if v < val:
      l = m
    else:
      r = m
  return r

class Solution:
  def findNumberOfLIS(self, nums):
    if not nums: return 0
    N = len(nums)
    l, dp = 0, [[] for _ in range(N)]
    for n in nums:
      idx1 = bs_left(dp, n, lambda _: _[-1][0] if _ else sys.maxsize)
      if idx1 == l:
        l += 1
      if idx1 == 0:
        dp[0].append((n, (dp[0][-1][1] if dp[0] else 0) + 1))
      else:
        idx2 = bs(dp[idx1 - 1], -n, lambda _: -_[0])
        dp[idx1].append((n, (dp[idx1][-1][1] if dp[idx1] else 0) + (
        dp[idx1 - 1][-1][1] if idx2 == 0 else (dp[idx1 - 1][-1][1] - dp[idx1 - 1][idx2 - 1][1]))))
      print(dp)
    return dp[l - 1][-1][1]

s = Solution()
print(s.findNumberOfLIS([1,3,5,4,3,3,1,8,6,7]))
