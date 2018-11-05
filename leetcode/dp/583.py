# https://leetcode.com/problems/delete-operation-for-two-strings/description/
# http://bit.ly/2jemDkt

class Solution:
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m, n = len(word1), len(word2)
    word1 = ' ' + word1
    word2 = ' ' + word2
    memo = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if word1[i] == word2[j]:
          memo[i][j] = 1 + memo[i - 1][j - 1]
        else:
          memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
    return m + n - 2 * memo[-1][-1]

class Solution:
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    cur = list(range(len(word2) + 1))
    nxt = [600] * (len(word2) + 1)
    for w1 in word1:
      nxt[0] = cur[0] + 1
      for i, w2 in enumerate(word2, 1):
        nxt[i] = min(cur[i], nxt[i - 1]) + 1
        if w1 == w2:
          nxt[i] = min(nxt[i], cur[i - 1])
      cur, nxt = nxt, cur
    return cur[-1]

assert Solution().minDistance("sea", "eat") == 2