# https://leetcode.com/problems/spiral-matrix/description/
# http://bit.ly/2IN2Lk1

class Solution:
  def spiralOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])