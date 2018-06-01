# https://leetcode.com/problems/course-schedule/description/
# http://bit.ly/2J1lCeX
# topological sort

class Solution:
  def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    visit, g = [0] * numCourses, [[] for _ in range(numCourses)]
    for x, y in prerequisites:
      g[x].append(y)

    def dfs(num):
      if visit[num] == 1:
        return True
      elif visit[num] == -1:
        return False
      visit[num] = -1
      for num_ in g[num]:
        if not dfs(num_):
          return False
      visit[num] = 1
      return True
    return all(dfs(n) for n in range(numCourses))

class Solution:
  def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    inDegrees, g = [0] * numCourses, [[] for _ in range(numCourses)]
    roots, alives = [], set()

    for x, y in prerequisites:
      inDegrees[x] += 1
      g[y].append(x)

    for i, indegree in enumerate(inDegrees):
      if indegree == 0:
        roots.append(i)
      else:
        alives.add(i)

    while roots:
      root = roots.pop()
      for out in g[root]:
        inDegrees[out] -= 1
        if inDegrees[out] == 0:
          roots.append(out)
          alives.remove(out)
    return not alives

