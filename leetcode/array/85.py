# https://leetcode.com/problems/maximal-rectangle/description/
# http://bit.ly/2JZ7L4u

class Solution:
  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
      return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0
    for row in matrix:
      for i in range(n):
        height[i] = height[i] + 1 if row[i] == '1' else 0
      stack = [-1]
      for i in range(n + 1):
        while height[i] < height[stack[-1]]:
          ans = max(ans, height[stack.pop()] * i - 1 - stack[-1])
        stack.append(i)
    return ans
