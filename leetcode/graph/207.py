# https://leetcode.com/problems/course-schedule/

from collections import defaultdict

from collections import deque
class Solution:
  def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    inDegrees = [0] * numCourses
    outNodes = [[] for _ in range(numCourses)]

    for pre in prerequisites:
      inDegrees[pre[0]] += 1
      outNodes[pre[1]].append(pre[0])

    roots = []
    alives = set()
    for i, indegree in enumerate(inDegrees):
      if indegree == 0:
        roots.append(i)
      else:
        alives.add(i)

    while roots:
      root = roots.pop()
      for out in outNodes[root]:
        inDegrees[out] -= 1
        if inDegrees[out] == 0:
          roots.append(out)
          alives.remove(out)

    return not alives

class Solution:
  def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if len(prerequisites) == 0:
      return True

    graph = defaultdict(lambda: ({
      'inDegree': 0,
      'outNodes': [],
    }))
    visited = set()

    for p1, p2 in prerequisites:
      graph[p1]['inDegree'] += 1
      graph[p2]['outNodes'].append(p1)

    front = [c for c in range(numCourses) if graph[c]['inDegree'] == 0]

    while len(front):
      node = front.pop()
      visited.add(node)
      for p2 in graph[node]['outNodes']:
        graph[p2]['inDegree'] -= 1
        if graph[p2]['inDegree'] == 0:
          front.append(p2)

    return len(visited) == numCourses

assert Solution().canFinish(1, [])
assert Solution().canFinish(2, [[1, 0]])
assert Solution().canFinish(2, [[1, 0],[0, 1]]) == False
assert Solution().canFinish(3, [[1, 0]])
