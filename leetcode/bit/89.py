# https://leetcode.com/problems/gray-code/description/

class Solution:
  def grayCode(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    return [(i >> 1) ^ i for i in range(1 << n)]
