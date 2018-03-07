# https://leetcode.com/problems/container-with-most-water/description/
# http://bit.ly/2t3uQQ2
class Solution:
  def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height) - 1
    m = 0
    while l != r:
      if height[l] > height[r]:
        m = max(m, (r - l) * height[r])
        r -= 1
      else:
        m = max(m, (r - l) * height[l])
        l += 1

    return m

