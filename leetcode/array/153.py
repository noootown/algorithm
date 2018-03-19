# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# http://bit.ly/2D8fWb5

import bisect

class Solution:
  def findMin(self, nums):
    self.__getitem__ = lambda i: nums[i] <= nums[-1]
    return nums[bisect.bisect(self, False, 0, len(nums))]

s = Solution()
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))