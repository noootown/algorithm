# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# http://bit.ly/2D8fWb5

import bisect

class Solution:
  def findMin(self, nums):
    return nums[bisect.bisect([_ <= nums[-1] for _ in nums], False)]
