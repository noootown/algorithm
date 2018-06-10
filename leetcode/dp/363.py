# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/

class Solution:
  def maxSumSubmatrix(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * range(n)] * range(m)


print(Solution().maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))