# https://leetcode.com/problems/unique-letter-string/description/
# http://bit.ly/2Ldm3Qy

class Solution:
  def uniqueLetterString(self, S):
    """
    :type S: str
    :rtype: int
    """
    index = {c: [-1, -1] for c in string.ascii_uppercase}
    res = 0
    for i, c in enumerate(S):
      k, j = index[c]
      res += (i - j) * (j - k)
      index[c] = [j, i]
    for c in index:
      k, j = index[c]
      res += (len(S) - j) * (j - k)
    return res % (10 ** 9 + 7)
