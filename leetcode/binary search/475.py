# https://leetcode.com/problems/heaters/description/
# http://bit.ly/2rsRjmw

from bisect import bisect

class Solution:
  def findRadius(self, houses, heaters):
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    heaters.sort()
    heaters1 = set(heaters)
    rslt = 0
    for h in houses:
      if h not in heaters1:
        pos = bisect(heaters, h)
        if pos == 0:
          rslt = max(rslt, heaters[0] - h)
        elif pos == len(heaters):
          rslt = max(rslt, h - heaters[-1])
        else:
          rslt = max(rslt, min(h - heaters[pos - 1], heaters[pos] - h))
    return rslt

class Solution:
  def findRadius(self, houses, heaters):
    """
    :type houses: List[int]
    :type heaters: List[int]
    :rtype: int
    """
    houses.sort()
    heaters.sort()
    heaters = [float('-inf')] + heaters + [float('inf')]  # add 2 fake heaters
    ans, i = 0, 0
    for house in houses:
      while house > heaters[i + 1]:  # search to put house between heaters
        i += 1
      ans = max(ans, min(house - heaters[i], heaters[i + 1] - house))
    return ans

Solution().findRadius([1,2,3],  [2])