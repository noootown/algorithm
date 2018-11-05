# https://leetcode.com/problems/single-number-iii/description/
# http://bit.ly/2rxLkfo
# https://goo.gl/Z7aBWw

class Solution:
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    a = b = 0
    for n in nums:
      a ^= n
    for n in nums:
      if n & a & -a:
        print(n)
        b ^= n;

    return [a ^ b, b]

# [5, 3]
Solution().singleNumber([1,2,1,3,2,5])
