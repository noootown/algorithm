# https://leetcode.com/problems/longest-increasing-subsequence/description/
# http://bit.ly/2HrHv2W
# https://www.youtube.com/watch?v=CE2b_-XfVDk
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# Longest Increasing Subsequence

class Solution:
  def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tails = [0] * len(nums)
    size = 0
    for x in nums:
      i, j = 0, size
      while i != j:
        m = (i + j) // 2
        if tails[m] < x:
          i = m + 1
        else:
          j = m
      tails[i] = x
      size = max(i + 1, size)
    return size

s = Solution()
s.lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])

class Solution:
  def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0

    N = len(nums)
    memo = [nums[0]]
    maxans = 1
    for num in nums[1:]:
      if num > memo[-1]:
        memo.append(num)
      else:
        # maxans = max(maxans, len(memo))
        idx = bisect.bisect_left(memo, num)
        memo[idx] = num
        # memo = memo[:idx+1]
    maxans = max(maxans, len(memo))
    return maxans

'''
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 4, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 2, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 2, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 2, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 2, 6, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 6, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 6, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 5, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 5, 9, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 3, 9, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 3, 9, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 3, 7, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 3, 7, 11, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
