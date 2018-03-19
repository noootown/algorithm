# https://leetcode.com/problems/triangle/description/
# http://bit.ly/2H24xvL

from functools import reduce

class Solution:
  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    return reduce(lambda a, b: [f + min(d, e) for d, e, f in zip(a, a[1:], b)], triangle[::-1])[0]
