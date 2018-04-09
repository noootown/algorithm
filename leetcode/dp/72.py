# https://leetcode.com/problems/edit-distance/description/
# https://www.youtube.com/watch?v=We3YDTzNXEk&t=191s

# The solution of the youtube can be reduced to space complexity with O(n)

class Solution:
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if len(word1) == 0:
      return len(word2)
    elif len(word2) == 0:
      return len(word1)

    dp = list(range(len(word2) + 1))

    for i, w1 in enumerate(word1):
      dp_ij, dp[0] = i, i + 1
      for j, w2 in enumerate(word2):
        if w1 == w2:
          dp_ij, dp[j + 1] = dp[j + 1], dp_ij
        else:
          dp_ij, dp[j + 1] = dp[j + 1], min(dp[j], dp[j + 1], dp_ij) + 1

    return dp[-1]
