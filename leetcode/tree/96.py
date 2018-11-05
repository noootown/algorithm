# https://leetcode.com/problems/unique-binary-search-trees/
# https://goo.gl/xcJrab

import math

class Solution:
  def numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """

    # DP
    res = [0] * (n + 1)
    res[0] = 1
    for i in range(1, n + 1):
      for j in range(i):
        res[i] += res[j] * res[i - 1 - j]
    return res[n]

# https://goo.gl/xcJrab
class Solution:
  def numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """

    # Catalan Number  (2n)!/((n+1)!*n!)
    return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))