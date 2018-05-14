# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
# http://bit.ly/2ruWIJw

class Solution:
  def findLongestWord(self, s, d):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """

    def isSubsequence(x):
      it = iter(s)
      return all(c in it for c in x)

    return min([dd for dd in d if isSubsequence(dd)] + [''], key=lambda x: (-len(x), x))
