# https://leetcode.com/problems/repeated-substring-pattern/description/
# http://bit.ly/2HHoV72

class Solution:
  def repeatedSubstringPattern(self, s):
    """
    :type s: str
    :rtype: bool
    """
    return s and s in (s + s)[1:-1]
