# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# http://bit.ly/2G4lHca

class Solution:
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    # 188
    # O(kN) time complexity and O(k) space complexity
    # correct and general solution for all k
    # if k is infinity, space complexity can be reduced to O(1)
    if k == 0:
      return 0
    elif k >= len(prices) / 2:
      return sum(prices[i] - prices[i - 1] for i in range(1, len(prices)) if prices[i] > prices[i - 1])

    buy = [-999999999] * (k + 1)
    buySell = [0] * (k + 1)

    for p in prices:
      for i in range(k, 0, -1):
          buySell[i] = max(buySell[i], buy[i] + p)
          buy[i] = max(buy[i], buySell[i-1] - p)
    return buySell[-1]


    # written by me
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