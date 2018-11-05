# https://leetcode.com/problems/gray-code/

class Solution:
  def grayCode(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    return [i ^ (i >> 1) for i in range(1 << n)]

# https://goo.gl/cg1HqL
class Solution:
  def grayCode(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    results = [0]
    for i in range(n):
      results += [x + pow(2, i) for x in reversed(results)]
    return results