# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
  def kthSmallest(self, matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    l, h  = matrix[0][0], matrix[-1][-1]
    while l < h:
      mid, cnt, j = l + (h - l) // 2, 0, len(matrix) - 1
      for m in matrix:
        while j >= 0 and m[j] > mid:
          j -= 1
        cnt += j + 1

      if cnt < k:
        l = mid + 1
      else:
        h = mid

    return l