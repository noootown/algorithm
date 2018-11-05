# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
  def findDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for x in nums:
      if nums[abs(x) - 1] < 0:
        res.append(abs(x))
      else:
        nums[abs(x) - 1] *= -1
    return res

class Solution:
  def findDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    check = [0] * (len(nums) + 1)
    duplicates = []
    for i in nums:
      if check[i]:
        duplicates.append(i)
      else:
        check[i] = 1

    return duplicates