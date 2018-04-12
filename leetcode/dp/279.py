# https://leetcode.com/problems/perfect-squares/description/
# http://bit.ly/2HqiO6J
# http://bit.ly/2HpNxkx
import math

# memoization
class Solution:
  """
  :type n: int
  :rtype: int
  """
  _dp = [0]
  def numSquares(self, n):
    dp = self._dp
    while len(dp) <= n:
      dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
    return dp[n]

class Solution:
  def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    while (n % 4 == 0):
      n = n / 4
    if n % 8 == 7: return 4;
    a = int(0)
    while (a * a <= n):
      b = int(math.sqrt(n - a * a))
      if (a * a + b * b == n):
        print('a=', a, 'b+', b)
        return (not not a) + (not not b)
      a += 1
    return 3