# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
# http://bit.ly/2IKalvE

# Longest common substring

class Solution:
  def findLength(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    for i, a in enumerate(A):
      for j, b in enumerate(B):
        if a == b:
          dp[i+1][j+1] = dp[i][j] + 1

    return max(max(row) for row in dp)
