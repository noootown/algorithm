# https://leetcode.com/problems/2-keys-keyboard/

# there's also dp solution, but slower
class Solution:
  def minSteps(self, n):
    """
    :type n: int
    :rtype: int
    """
    fac = []
    while (n % 2 == 0):
      fac.append(2)
      n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
      while n % i == 0:
        fac.append(i)
        n = n / i
    if n > 2:
      fac.append(n)
    return int(sum(fac))
