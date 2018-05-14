# https://leetcode.com/problems/single-number-iii/description/
# http://bit.ly/2rxLkfo

class Solution:
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    a = b = 0
    for n in nums:
      a ^= n
    for n in nums:
      if n & a & -a:
        b ^= n;
    return [a ^ b, b]
