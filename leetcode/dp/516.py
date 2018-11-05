# https://leetcode.com/problems/longest-palindromic-subsequence/description/
# http://bit.ly/2Ftizpc

class Solution:
  def longestPalindromeSubseq(self, s):
    """
    :type s: str
    :rtype: int
    """
    if s == s[::-1]:
      return len(s)

    N = len(s)
    dp = [0] * N

    for i in range(0, len(dp)):
      tmp_dp = dp[:]
      tmp_dp[i] = 1
      for j in range(i-1, -1, -1):
        if s[i] == s[j]:
          tmp_dp[j] = 2 + dp[j + 1]
        else:
          tmp_dp[j] = max(dp[j], tmp_dp[j + 1])
      dp = tmp_dp
    return dp[0]

assert Solution().longestPalindromeSubseq('bbbab') == 4
