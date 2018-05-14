# https://leetcode.com/problems/number-complement/description/
# http://bit.ly/2G1kHof

class Solution:
  def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    mask = num
    mask |= mask >> 1
    mask |= mask >> 2
    mask |= mask >> 4
    mask |= mask >> 8
    mask |= mask >> 16
    return num ^ mask

class Solution:
  def findComplement(self, num):
    """
    :type num: int
    :rtype: int
    """
    i = 1
    while i <= num:
      i <<= 1
    return (i - 1) ^ num