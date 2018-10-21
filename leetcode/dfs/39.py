# https://leetcode.com/problems/combination-sum/submissions/

class Solution:
  def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    candidates.sort()

    def dfs(target, result):
      if not target:
        res.append(result)
      else:
        for item in candidates:
          if item > target:
            break
          elif not result or item >= result[-1]:
            dfs(target - item, result + [item])

    dfs(target, [])
    return res