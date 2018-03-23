# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

class Solution:
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy, buySell, buySellPre = -9999999999, 0, 0

    for p in prices:
      oldBuySell = buySell
      buySell = max(buySell, buy + p)
      buy = max(buy, buySellPre - p)
      buySellPre = oldBuySell

    return buySell
