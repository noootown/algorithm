# https://leetcode.com/problems/reverse-vowels-of-a-string/
# http://bit.ly/2H7sjLs

import re

class Solution:
  def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
