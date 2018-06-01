# https://leetcode.com/problems/course-schedule-ii/description/
# similar to 204

class Solution:
  def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    visit, g = [0] * numCourses, [[] for _ in range(numCourses)]
    for x, y in prerequisites:
      g[x].append(y)

    def dfs(num, p):
      if visit[num] == 1:
        return True
      elif visit[num] == -1:
        return False
      visit[num] = -1
      for num_ in g[num]:
        if not dfs(num_, path):
          return False
      path.append(num)
      visit[num] = 1
      return True

    path = []
    for n in range(numCourses):
      p = []
      if not dfs(n, p):
        return []
      path.extend(p)
    return path

class Solution:
  def findOrder(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    indeg, g = [0] * numCourses, [[] for _ in range(numCourses)]
    roots, alives = [], set()

    for p, r in prerequisites:
      g[p].append(r)
      indeg[r] += 1

    for i, indegree in enumerate(indeg):
      if indegree == 0:
        roots.append(i)
      else:
        alives.add(i)

    path = []

    while roots:
      root = roots.pop()
      path.append(root)
      for out in g[root]:
        indeg[out] -= 1
        if indeg[out] == 0:
          roots.append(out)
          alives.remove(out)

    return path[::-1] if not alives else []
