# https://leetcode.com/problems/out-of-boundary-paths/description/
# http://bit.ly/2HC3OlR

class Solution:
  def findPaths(self, m, n, N, i, j):
    """
    :type m: int
    type n: int
    :type N: int
    :type i: int
    :type j: int
    :rtype: int
    """
    MOD = 10 ** 9 + 7

    def binom_all(n):
      ans = [1]
      r = 1
      for i in range(1, n + 1):
        r *= n - i + 1
        r //= i
        ans.append(r)
      return ans

    def solve_1D(A):
      ans = [1]
      for time in range(N + 1):
        Anew = [0] * len(A)
        inside = 0
        for i, u in enumerate(A):
          if i >= 1:
            Anew[i - 1] += u
            inside += u
          if i < len(A) - 1:
            Anew[i + 1] += u
            inside += u
        A = Anew
        ans.append(inside)
      return ans

    dprow = solve_1D([+(r == i) for r in range(m)])
    dpcol = solve_1D([+(c == j) for c in range(n)])
    binoms = [binom_all(n) for n in range(N + 1)]

    def inside(t):
      return sum(dprow[k] * dpcol[t - k] * binoms[t][k] for k in range(t + 1)) % MOD

    return (3 * sum(inside(t) for t in range(N)) - inside(N) + inside(0)) % MOD

s = Solution()
print(s.findPaths(m = 2, n = 2, N = 2, i = 0, j = 0))