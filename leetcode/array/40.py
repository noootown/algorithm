# https://leetcode.com/problems/combination-sum-ii/description/
# http://bit.ly/2ILn7dn

class Solution:
  def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    table = [None] + [set() for i in range(target)]
    for i in candidates:
      if i > target:
        break
      for j in range(target - i, 0, -1):
        table[i + j] |= {elt + (i,) for elt in table[j]}
      table[i].add((i,))
    return [*map(list, table[target])]

s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))