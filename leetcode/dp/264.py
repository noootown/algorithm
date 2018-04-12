# https://leetcode.com/problems/ugly-number-ii/description/
# http://bit.ly/2HoOWrs

class Solution:
  def nthUglyNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    uglyPrime = [2, 3, 5]
    uglyList = [1]
    uglyPtr = [0] * len(uglyPrime)

    for i in range(n - 1):
      uglyList.append(min(uglyList[uglyPtr[i]] * p for i, p in enumerate(uglyPrime)))
      for i, p in enumerate(uglyPrime):
        if uglyList[-1] == uglyList[uglyPtr[i]] * p:
          uglyPtr[i] += 1

    return uglyList[-1]
