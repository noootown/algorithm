# https://leetcode.com/problems/can-i-win/description/
# https://leetcode.com/submissions/detail/150313692/

# answer 1
class Solution:
  def canIWin(self, maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    dp = dict()

    def search(state, total):
      # me can win or not
      for x in range(maxChoosableInteger, 0, -1):
        if not state & (1 << (x - 1)):
          if total + x >= desiredTotal:
            dp[state] = True
            return True
          break

      # opponent can't win or not
      for x in range(1, maxChoosableInteger + 1):
        if not state & (1 << (x - 1)):
          nstate = state | (1 << (x - 1))
          if nstate not in dp:
            dp[nstate] = search(nstate, total + x)
          if not dp[nstate]:
            dp[state] = True
            return True
      dp[state] = False
      return False

    if maxChoosableInteger >= desiredTotal:
      return True
    if (1 + maxChoosableInteger) * maxChoosableInteger < 2 * desiredTotal:
      return False
    return search(0, 0)

# answer 2
class Solution:
  def canIWin(self, maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
      return False
    self.memo = {}
    return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)

  def helper(self, nums, desiredTotal):
    hash = str(nums)
    if hash in self.memo:
      return self.memo[hash]

    if nums[-1] >= desiredTotal:
      return True

    for i in range(len(nums)):
      # opponent can't win
      if not self.helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):
        self.memo[hash] = True
        return True
    self.memo[hash] = False
    return False