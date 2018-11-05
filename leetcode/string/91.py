# https://leetcode.com/problems/decode-ways/

class Solution:
  def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """

    if s == '':
      return 0

    prev, ans = 1, int(s[0] > '0')

    for s1, s2 in zip(s, s[1:]):
      prev, ans = ans, ans * (s2 > '0') + prev * (9 < int(s1 + s2) < 27)

    return ans

assert Solution().numDecodings('12') == 2
assert Solution().numDecodings('226') == 3
assert Solution().numDecodings('0') == 0
assert Solution().numDecodings('00') == 0
