# https://leetcode.com/problems/maximum-subarray/description/
# http://bit.ly/2G5bxZJ
# https://en.wikipedia.org/wiki/Maximum_subarray_problem

class Solution:
  def maxSubArray(self, nums):
    if not nums:
      return 0

    curSum, maxSum = nums[0], nums[0]

    for n in nums[1:]:
      curSum = max(n, curSum + n)
      maxSum = max(curSum, maxSum)

    return maxSum