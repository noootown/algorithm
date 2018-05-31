# https://leetcode.com/problems/permutations/description/
# http://bit.ly/2kDDsGg

class Solution:
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]
