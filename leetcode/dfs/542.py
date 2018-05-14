# https://leetcode.com/problems/01-matrix/description/

class Solution:
  def updateMatrix(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
      for j in range(n):
        if matrix[i][j] != 0:
          matrix[i][j] = min(matrix[i - 1][j] + 1 if i - 1 >= 0 else 0x7FFFFFFF,
                             matrix[i][j - 1] + 1 if j - 1 >= 0 else 0x7FFFFFFF)

    for i in range(m - 1, -1, -1):
      for j in range(n - 1, -1, -1):
        if matrix[i][j] != 0:
          matrix[i][j] = min(matrix[i][j], matrix[i + 1][j] + 1 if i + 1 < m else 0x7FFFFFFF,
                             matrix[i][j + 1] + 1 if j + 1 < n else 0x7FFFFFFF)

    return matrix
