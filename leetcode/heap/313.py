# https://leetcode.com/problems/super-ugly-number/description/
# http://bit.ly/2GVaCi9
import heapq

class Solution:
  def nthSuperUglyNumber(self, n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    uglies = [1]

    def gen(prime):
      return (ugly * prime for ugly in uglies)

    merged = heapq.merge(*(gen(p) for p in primes))
    while len(uglies) < n:
      ugly = next(merged)
      if ugly != uglies[-1]:
        uglies.append(ugly)
    return uglies[-1]

s = Solution()
print(s.nthSuperUglyNumber(12, [2, 7, 13, 19]))
