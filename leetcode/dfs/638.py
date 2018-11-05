# https://leetcode.com/problems/shopping-offers/

class Solution:
  def shoppingOffers(self, price, special, needs):
    """
    :type price: List[int]
    :type special: List[List[int]]
    :type needs: List[int]
    :rtype: int
    """
    self.p = 999999999

    def dfs(needs, p):
      if all(nn == 0 for nn in needs):
        self.p = min(self.p, p)
        return

      self.p = min(self.p, p + sum((nn if nn >= 0 else 0) * pp for nn, pp in zip(needs, price)))

      for s in special:
        needs_ = [nn - ss for ss, nn in zip(s, needs)]
        if all(nn >= 0 for nn in needs_):
          dfs(needs_, p + s[-1])

    dfs(needs, 0)
    return self.p

assert Solution().shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]) == 14
assert Solution().shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]) == 11