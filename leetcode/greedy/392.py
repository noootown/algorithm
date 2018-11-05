# https://leetcode.com/problems/is-subsequence/

class Solution:
  def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    t = iter(t)
    return all(c in t for c in s)
  