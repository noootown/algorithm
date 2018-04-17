# https://leetcode.com/problems/ransom-note/description/
# http://bit.ly/2H4EdFD

from collections import Counter

class Solution:
  def canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    return not Counter(ransomNote) - Counter(magazine)
