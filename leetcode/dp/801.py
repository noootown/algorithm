# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/
# http://bit.ly/2HEQb5U

class Solution:
  def minSwap(self, A, B):
    same, swap = 0, 1
    for a1, a2, b1, b2 in zip(A, A[1:], B, B[1:]):
      if a2 <= a1 or b2 <= b1:
        same, swap = swap, same
      elif b2 > a1 and a2 > b1:
        same = swap = min(swap, same)
      swap += 1
    return min(same, swap)
