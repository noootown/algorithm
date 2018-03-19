# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

class Solution:
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    # 188
    # O(kN) time complexity and O(1) space complexity
    # if k == 0:
    #   return 0
    # elif k >= len(prices) / 2:
    #   return sum(prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1])
    #
    # buy = [-999999999] * (k + 1)
    # buySell = [0] * (k + 1)
    #
    # for p in prices:
    #   for i in range(k, 0, -1):
    #       buySell[i] = max(buySell[i], buy[i] + p)
    #       buy[i] = max(buy[i], buySell[i-1] - p)
    # return buySell[-1]

    # O(kN) time complexity and O(N) space complexity
    k = 2
    buy = [-999999999] * k
    buySell = [0] * k

    for p in prices:
      for i in range(k):
        buy[i] = max(buy[i], buySell[i - 1] - p if i != 0 else -p)
        buySell[i] = max(buySell[i], buy[i] + p)

    return buySell[-1]

    # O(N^2)
    # def findHigh(prices):
    #   minPrice = 99999999
    #   maxProfit = 0
    #   for p in prices:
    #     if p < minPrice:
    #       minPrice = p
    #     elif p - minPrice > maxProfit:
    #       maxProfit = p - minPrice
    #   return maxProfit
    #
    # minPrice = 99999999
    # maxProfit = 0
    # for i, p in enumerate(prices[:-1]):
    #   if p > minPrice:
    #     maxProfit = max(findHigh(prices[:i + 1]) + findHigh(prices[i + 1:]), maxProfit)
    #   else:
    #     minPrice = p
    #
    # return max(maxProfit, findHigh(prices))