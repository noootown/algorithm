# https://leetcode.com/problems/network-delay-time/description/
# http://bit.ly/2ou0ulb
import heapq
from collections import defaultdict

class Solution:
  def networkDelayTime(self, times, N, K):
    """
    :type times: List[List[int]]
    :type N: int
    :type K: int
    :rtype: int
    """
    pq = []
    visitNode = set()

    src = defaultdict(list)
    for u, v, w in times:
      src[u].append((v, w))

    heapq.heappush(pq, (0, K))
    res = 0

    while pq and len(visitNode) != N:
      curnode = heapq.heappop(pq)
      visitNode.add(curnode[1])
      res = curnode[0]
      for target, t in src[curnode[1]]:
        if target in visitNode: continue
        heapq.heappush(pq, (t + curnode[0], target))

    return res if len(visitNode) == N else -1

a = Solution()
print(a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
# print(a.networkDelayTime([[1,2,1]], 2, 2))
