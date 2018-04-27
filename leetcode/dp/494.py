# https://leetcode.com/problems/target-sum/description/
# http://bit.ly/2I2SVdP
# http://bit.ly/2I4RBqw
# related to 416

# ans1
class Solution:
  def findTargetSumWays(self, nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    if not nums:
      return 0
    dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
    for i in range(1, len(nums)):
      tdic = {}
      for d in dic:
        tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
        tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
      dic = tdic
    return dic.get(S, 0)

# ans2
class Solution:
  def findTargetSumWays(self, nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    c = [1] + [0] * 1000
    T = sum(nums)
    A = T + S
    if T < S or A & 1:
      return 0
    A >>= 1
    temp = 0
    for v in sorted(nums):
      temp += v
      for i in range(min(temp, A), v - 1, -1):
        c[i] += c[i - v]
    return c[A]
