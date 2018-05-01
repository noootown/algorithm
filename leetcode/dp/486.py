# https://leetcode.com/problems/predict-the-winner/description/
# http://bit.ly/2HBgTjf
# http://bit.ly/2r82uQw

class Solution:
  def PredictTheWinner(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    if n == 1 or n % 2 == 0: return True
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
      for j in range(i + 1, n):
        dp[i][j] = max(nums[j] - dp[i][j - 1], nums[i] - dp[i + 1][j])
    return dp[0][-1] >= 0
