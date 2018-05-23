# https://leetcode.com/problems/single-number-ii/description/
# http://bit.ly/2LhpdTw
# http://bit.ly/2Leke5O

class Solution:
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ones = twos = 0
    for n in nums:
      ones = (ones ^ n) & ~twos
      twos = (twos ^ n) & ~ones
    return ones

class Solution:
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = b = 0
    for c in nums:
      a, b = (~a & b & c) | (a & ~b & ~c), (~a & ~b & c) | (~a & b & ~c)
    return a | b

print(Solution().singleNumber([0,2,1,0,99,1,2,2,0,1]))