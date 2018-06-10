# https://leetcode.com/problems/hand-of-straights/description/

from collections import Counter

class Solution:
  def isNStraightHand(self, hand, W):
    """
    :type hand: List[int]
    :type W: int
    :rtype: bool
    """
    if len(hand) % W != 0:
      return False

    m = Counter(hand)
    seq, ptr = sorted(m.keys()), 0
    while 1:
      while ptr < len(seq) and m[seq[ptr]] == 0:
        ptr += 1
      if ptr == len(seq):
        return True
      for i in range(W):
        m[seq[ptr]+i] -= 1
        if m[seq[ptr]+i] < 0:
          return False


print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(Solution().isNStraightHand([1,2,3,4,5], 4))
print(Solution().isNStraightHand([1,2,3,4,5,7,8,9], 4))
