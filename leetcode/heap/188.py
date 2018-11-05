# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/#/description

from heapq import heappush, heappop

class Solution:
  def maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if k == 0:
      return 0
    elif k >= len(prices) / 2:
      return sum(prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1])

    buy = [-999999999] * (k + 1)
    buySell = [0] * (k + 1)

    for p in prices:
      for i in range(k, 0, -1):
        buySell[i] = max(buySell[i], buy[i] + p)
        buy[i] = max(buy[i], buySell[i - 1] - p)
    return buySell[-1]

class Solution:
  def maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    length = len(prices)
    if length < 2 or k < 1:
      return 0

    if k >= length // 2:
      return sum(prices[i] - prices[i - 1] for i in range(1, length) if prices[i] - prices[i - 1] > 0)

    profit, pairs, j = [], [], 0

    while j < length:
      i = j
      # find local lowest point
      while i < length - 1 and prices[i] >= prices[i + 1]:
        i += 1
      j = i + 1
      # find local highest point
      while j < length and prices[j] >= prices[j - 1]:
        j += 1

      while pairs and prices[i] < prices[pairs[-1][0]]:
        lo, hi = pairs.pop()
        heappush(profit, prices[lo] - prices[hi])
      while pairs and prices[j - 1] >= prices[pairs[-1][1]]:
        lo, hi = pairs.pop()
        heappush(profit, prices[i] - prices[hi])
        i = lo

      pairs.append([i, j - 1])

    while pairs:
      lo, hi = pairs.pop()
      heappush(profit, prices[lo] - prices[hi])

    ans = 0
    while k > 0 and profit:
      # default is min heap
      ans -= heappop(profit)
      k -= 1

    return ans

assert Solution().maxProfit(2, [2,4,1]) == 2
assert Solution().maxProfit(3, [2,4,6,8,10,12,1,5,9,3,20,19,6,15]) == 38
