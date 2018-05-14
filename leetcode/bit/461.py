# https://leetcode.com/problems/hamming-distance/description/
# http://bit.ly/2jKuC91
# http://bit.ly/2jMsFZP

class Solution:
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    h = 0
    while x != 0 or y != 0:
      h += x & 1 != y & 1
      x >>= 1
      y >>= 1
    return h

class Solution:
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    x, y = x ^ y, 0
    while x:
      y += 1
      x &= x - 1
    return y
  # 1101 -> 1100 -> 1000 -> 0000 => 3 1's

class Solution:
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x ^ y).count('1')