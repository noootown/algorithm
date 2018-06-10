# https://leetcode.com/problems/different-ways-to-add-parentheses/description/

import re

class Solution:
  def diffWaysToCompute(self, input):
    """
    :type input: str
    :rtype: List[int]
    """
    num = [int(_) for _ in re.findall('(\d+)', input)]
    sign = re.findall('([\+\-\*])', input)
    N = len(num)
    dp = [[[] for _ in range(N-i)]  for i in range(N)]

    for i in range(N):
      dp[0][i].append(num[i])

    for i in range(1, N):
      for j in range(N-i):
        for k in range(i):
          for l in dp[i-k-1][j]:
            for r in dp[k][j+i-k]:
              if sign[j+i-k-1] == '+':
                dp[i][j].append(l+r)
              elif sign[j+i-k-1] == '-':
                dp[i][j].append(l-r)
              elif sign[j+i-k-1] == '*':
                dp[i][j].append(l*r)
    return sorted(list(dp[-1][-1]))

class Solution:
  def diffWaysToCompute(self, input):
    """
    :type input: str
    :rtype: List[int]
    """
    if input.isdigit():
      return [int(input)]
    res = []
    for i in range(len(input)):
      if input[i] in '+-*':
        res1 = self.diffWaysToCompute(input[:i])
        res2 = self.diffWaysToCompute(input[i + 1:])
        for j in res1:
          for k in res2:
            res.append(self.helper(j, k, input[i]))
    return res
  def helper(self, j, k, op):
    if op == '+':
      return j + k
    elif op == '*':
      return j * k
    elif op == '-':
      return j - k

Solution().diffWaysToCompute("2*3-4*5")
