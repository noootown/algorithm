# https://leetcode.com/problems/continuous-subarray-sum/description/
# http://bit.ly/2HBtq6r

class Solution(object):
  def checkSubarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if 0 == k:
      return len(nums) >= 2 and any(i == 0 and j == 0 for i, j in zip(nums, nums[1:]))

    sums = 0
    ht = {0: -1}
    for i in range(len(nums)):
      sums += nums[i]
      rem = sums % k
      if rem in ht:
        if i - ht[rem] >= 2:
          return True
      else:
        ht[rem] = i
    return False