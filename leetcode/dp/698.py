# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
# http://bit.ly/2qvOIH2
# https://leetcode.com/submissions/detail/149971926/

class Solution:
  def canPartitionKSubsets(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    target, rem = divmod(sum(nums), k)
    if rem or max(nums) > target:
      return False
    seen = [0] * len(nums)
    nums.sort(reverse=True)

    def dfs(k, index, current_sum):
      if k == 1:
        return True
      if current_sum == target:
        return dfs(k - 1, 0, 0)

      for i in range(index, len(nums)):
        if not seen[i] and current_sum + nums[i] <= target:
          seen[i] = 1
          if dfs(k, i + 1, current_sum + nums[i]):
            return True
          seen[i] = 0
      return False

    return dfs(k, 0, 0)

s = Solution()
print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
