# https://leetcode.com/problems/4sum/description/
# http://bit.ly/2t8eDcv

class Solution:
  def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def findNSum(arr, target, N, result, results):
      if len(arr) < N or N < 2 or arr[0] * N > target or arr[-1] * N < target:
        return

      if N == 2:
        l, r = 0, len(arr) - 1
        while l < r:
          s = arr[l] + arr[r]
          if s == target:
            results.append(result + [arr[l], arr[r]])
            l += 1
            while l < r and arr[l] == arr[l - 1]:
              l += 1
          elif s < target:
            l += 1
          else:
            r -= 1
      else:
        for i, n in enumerate(arr[:-N + 1]):
          if i == 0 or (i > 0 and arr[i - 1] != n):
            findNSum(arr[i + 1:], target - n, N - 1, result + [n], results)

    res = []
    findNSum(sorted(nums), target, 4, [], res)
    return res