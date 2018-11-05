# https://leetcode.com/problems/ones-and-zeroes/description/
# http://bit.ly/2FeQoKd

# timeout
# class Solution:
#   def findMaxForm(self, strs, m, n):
#     """
#     :type strs: List[str]
#     :type m: int
#     :type n: int
#     :rtype: int
#     """
#     dp = [[0] * n for _ in range(m)]
#
#     for z, o in [(s.count('0'), s.count('1')) for s in strs]:
#       for x in range(n, -1, -1):
#         for y in range(m, -1, -1):
#           if x >= z and y >= o:
#             dp[x][y] = max(dp[x-z][y-o] + 1, dp[x][y])

class Solution:
  def getMax(self, arr, m, n):
    res = 0

    for z, o in arr:
      if m >= z and n >= o:
        res += 1
        m -= z
        n -= o

    return res

  def findMaxForm(self, strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    arr = [(s.count('0'), s.count('1')) for s in strs]
    arr1 = sorted(arr, key=lambda s: -min(m - s[0], n - s[1]))
    arr2 = sorted(arr, key=lambda s: min(s[0], s[1]))
    res = max(self.getMax(arr1, m, n), self.getMax(arr2, m, n))

    return res

assert Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4
