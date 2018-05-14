# https://leetcode.com/problems/decode-string/description/
# http://bit.ly/2KSggji
import re

class Solution:
  def decodeString(self, s):
    """
    :type s: str
    :rtype: str
    """
    while '[' in s:
      s = re.sub(r'(\d+)\[([a-zA-Z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
    return s