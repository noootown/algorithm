# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/


class Solution:
  def maxProfit(self, prices, fee):
    """
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    buy = -9999999999
    buySell = 0

    for p in prices:
      oldBuySell = buySell
      buySell = max(buySell, buy + p)
      buy = max(buy, oldBuySell - p - fee)

    return buySell

    # buy, res = prices[0], 0
    # for p in prices:
    #   if buy > p:  # current price is less than last buy
    #     buy = p  # buy at p
    #   else:
    #     tmp = p - buy - fee
    #     if tmp > 0:  # have profit
    #       res += tmp
    #       buy = p - fee
    # return res