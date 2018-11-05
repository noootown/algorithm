# https://leetcode.com/problems/redundant-connection/

class Solution:
  def findRedundantConnection(self, edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    u = list(range(len(edges) + 1))

    def find(x):
      while x != u[x]:
        u[x] = u[u[x]]
        x = u[x]
      return x

    for i, j in edges:
      i_, j_ = find(i), find(j)
      if i_ != j_:
        u[j_] = i_
      else:
        return [i, j]
