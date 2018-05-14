# https://leetcode.com/problems/find-eventual-safe-states/description/
# http://bit.ly/2KdIkfY

class Solution:
  def eventualSafeNodes(self, graph):
    """
    :type graph: List[List[int]]
    :rtype: List[int]
    """
    n = len(graph)
    res = set([i for i in range(n) if not graph[i]])
    left = set(range(n)) - res
    while 1:
      flag = False
      for i in list(left):
        if set(graph[i]).issubset(res):
          res.add(i)
          left.remove(i)
          flag = True
      if not flag:
        break
    return sorted(list(res))