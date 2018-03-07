# https://leetcode.com/problems/subsets/description/
# http://bit.ly/2H0fazj

class Solution:
  def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # return [[nums[j] for j in range(len(nums)) if i & 1 << j] for i in range(1 << len(nums))]
    # return reduce(lambda L, ele: L + [l + [ele] for l in L], nums, [[]])
    # return [[x for x in l if x is not None] for l in itertools.product(*zip(nums, [None] * len(nums)))]
    # return [l for n in range(len(nums) + 1) for l in itertools.combinations(nums, n)]