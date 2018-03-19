# https://leetcode.com/problems/3sum/description/
# https://leetcode.com/submissions/detail/143009330/

import collections

class Solution:
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    counter = collections.Counter(nums)
    ans = [] if counter[0] < 3 else [[0, 0, 0]]

    ngs = sorted([x for x in counter if x < 0], reverse=True)
    n_ngs = sorted([x for x in counter if x >= 0])

    for n_ng in n_ngs:
      for ng in ngs:
        need = -(ng + n_ng)
        if need in counter:
          if (need == ng or need == n_ng) and counter[need] > 1:
            ans.append([ng, need, n_ng])
          elif need < ng:
            ans.append([need, ng, n_ng])
          elif n_ng < need:
            ans.append([ng, n_ng, need])
    return ans


