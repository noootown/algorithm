# https://leetcode.com/problems/contiguous-array/description/
# http://bit.ly/2jjOyiI

class Solution:
  def findMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    max_length = 0
    table = {0: -1}
    for i, num in enumerate(nums):
      count = count + 1 if num == 1 else count - 1
      if count in table:
        l = i - table[count]
        if l > max_length:
          max_length = l
      else:
        table[count] = i

    return max_length