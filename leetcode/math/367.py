# https://leetcode.com/problems/valid-perfect-square/description/
# http://bit.ly/2GUQMj3

# x^2 = 1 + 3 + 5 + .......
class Solution:
  def isPerfectSquare(self, num):
    """
    :type num: int
    :rtype: bool
    """
    i = 1
    while num > 0:
      num -= i
      i += 2

    return num == 0

# binary search
class Solution:
  def isPerfectSquare(self, num):
    """
    :type num: int
    :rtype: bool
    """
    low, high = 1, num
    while low <= high:
      mid = (low + high) >> 1
      if mid * mid == num:
        return True
      if mid * mid < num:
        low = mid + 1
      else:
        high = mid - 1
    return False

# Since we are solving x^2 - num = 0
# by Newton's method, x_{k+1} = x_k - f(x) / f'(x)
# x_{k+1} = x - (x^2 - num) / 2x
#         = (x - num / x) / 2

# Newton's method
class Solution:
  def isPerfectSquare(self, num):
    """
    :type num: int
    :rtype: bool
    """
    x = num
    while x**2 > num:
      x = (x + num//x) >> 1

    return x**2 == num
