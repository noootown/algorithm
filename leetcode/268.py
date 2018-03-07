# https://leetcode.com/problems/missing-number/description/
# http://bit.ly/2HZOb8j

class Solution:
  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    # return int(n * (n + 1) / 2 - sum(nums))
    # return reduce(operator.xor, nums + range(len(nums) + 1))
    # return reduce(operator.xor, nums) ^ [n, 1, n + 1, 0][n % 4]
    # return (set(range(n + 1)) - set(nums)).pop()