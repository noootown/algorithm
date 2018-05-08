# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# http://bit.ly/2rtdurX

class Solution:
  def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    heights.append(0)
    stk = [-1]
    ans = 0
    for i, h in enumerate(heights):
      while h < heights[stk[-1]]:
        s = heights[stk.pop()] * (i - stk[-1] - 1)
        ans = max(ans, s)
      stk.append(i)
    return ans
