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

class Solution:
  def decodeString(self, s):
    """
    :type s: str
    :rtype: str
    """
    stack = [[1, ""]]

    num = ''
    for ch in s:
      if ch.isdigit():
        num += ch
      elif ch == '[':
        stack.append([int(num), ""])
        num = ''
      elif ch == ']':
        k, word = stack.pop()
        stack[-1][1] += word * k
      else:
        stack[-1][1] += ch

    return stack[0][1]

assert(Solution().decodeString('3[a]2[bc]') == 'aaabcbc')
assert(Solution().decodeString('3[a2[c]]') == 'accaccacc')
assert(Solution().decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef')
