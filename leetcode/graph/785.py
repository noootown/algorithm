# https://leetcode.com/problems/is-graph-bipartite/description/
# http://bit.ly/2ryopkG
# http://bit.ly/2rAtd9e
from collections import deque

class Solution:
  def isBipartite(self, graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """
    n, colored = len(graph), {}

    def dfs_color(color, idx, colored):
      if idx in colored:
        return color == colored[idx]
      colored[idx] = color
      return all(dfs_color(-color, nb, colored) for nb in graph[idx])

    return all(i in colored or dfs_color(1, i, colored) for i in range(n))

class Solution:
  def isBipartite(self, graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """
    n, colored = len(graph), {}
    for i in range(n):
      if i not in colored and graph[i]:
        colored[i] = 1
        q = deque([i])
        while q:
          cur = q.popleft()
          for nb in graph[cur]:
            if nb not in colored:
              colored[nb] = -colored[cur]
              q.append(nb)
            elif colored[nb] == colored[cur]:
              return False
    return True