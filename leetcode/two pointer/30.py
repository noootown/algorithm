# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
# http://bit.ly/2ICm8vu
from collections import defaultdict

class Solution:
  def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if len(words) == 0:
      return []

    d, l, i, ans = defaultdict(int), len(words[0]), 0, []
    for w in words:
      d[w] += 1

    # sliding window(s)
    for k in range(l):
      left, subd, count = k, defaultdict(int), 0
      for j in range(k, len(s) - l + 1, l):
        tword = s[j:j + l]
        if tword in d:
          subd[tword] += 1
          count += 1
          while subd[tword] > d[tword]:
            subd[s[left:left + l]] -= 1
            left += l
            count -= 1
          if count == len(words):
            ans.append(left)
        else:
          left, subd, count = j + l, defaultdict(int), 0

    return ans
