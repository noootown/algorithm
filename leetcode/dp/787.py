# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# http://bit.ly/2HbWQTp

import collections
import heapq
# priority queue
# heapq default is a min heap

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1

# dynamic programming
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dp = [float('inf')] * n
        dp[src] = 0

        nowk = 0
        while nowk <= K:
            newdp = dp[:]
            for sc, dt, price in flights:
                newdp[dt] = min(newdp[dt], price + dp[sc])
            dp = newdp
            nowk += 1

        return -1 if dp[dst] == float('inf') else dp[dst]

s = Solution()

s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)