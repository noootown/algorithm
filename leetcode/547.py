# https://leetcode.com/problems/friend-circles/description/

class Solution:
  def findCircleNum(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    l = len(M)
    d, total = list(range(l)), 0

    def find(x):
      while d[x] != x:
        # d[x] = d[d[x]] # this line is used to reduce height
        x = d[x]
      return x

    cnt = l
    for i in range(l):
      for j in range(i + 1, l):
        if M[i][j]:
          i_, j_ = find(i), find(j)
          if i_ != j_:
            d[j_] = i_
            cnt -= 1
    return cnt
