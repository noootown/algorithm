# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
# http://bit.ly/2Lew3JA

class Solution:
  def findMaximumXOR(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    answer = 0
    for i in range(31, -1, -1):
      answer <<= 1
      prefixes = {num >> i for num in nums}
      answer += any(answer^1^p in prefixes for p in prefixes)
    return answer

assert Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28
