# https://leetcode.com/problems/palindromic-substrings/description/
# http://bit.ly/2HtnJXW
# http://bit.ly/2Hql6Gd

# ans1 116ms
class Solution:
  def countSubstrings(self, s):
    N = len(s)
    ans = 0
    for center in range(2 * N - 1):
      left = center / 2
      right = left + center % 2
      while left >= 0 and right < N and s[left] == s[right]:
        ans += 1
        left -= 1
        right += 1
    return ans

# ans2 44ms
class Solution:
  def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    ret = 0
    left, right = 0, 0
    while left < len(s):
      while right < len(s) and s[right] == s[left]:
        right += 1
      ret += sum(i for i in range(1, right - left + 1))
      l, r = left - 1, right
      while l >= 0 and r < len(s) and s[r] == s[l]:
        ret += 1
        l -= 1
        r += 1
      left = right
    return ret
