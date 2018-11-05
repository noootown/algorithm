# https://leetcode.com/problems/ipo/

import heapq

class Solution:
  def findMaximizedCapital(self, k, W, Profits, Capital):
    """
    :type k: int
    :type W: int
    :type Profits: List[int]
    :type Capital: List[int]
    :rtype: int
    """
    pro = sorted(list(zip(Profits, Capital)), key=lambda x: -x[1])
    h = []
    while k > 0:
      while pro and pro[-1][1] <= W:
        heapq.heappush(h, -pro.pop()[0])
      if not h:
        break
      W -= heapq.heappop(h)
      k -= 1
    return W