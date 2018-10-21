# https://leetcode.com/problems/first-missing-positive/description/

class Solution:
  def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ret = 1
    while ret < len(nums) + 1:
      if ret not in nums:
        return ret
      ret += 1
    return ret
