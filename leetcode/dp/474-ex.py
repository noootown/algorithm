class Solution:
  def getMax(self, arr, limit):
    res = 0
    limit_ = [l for l in limit]
    for a in arr:
      if all(l >= aa for aa, l in zip(a, limit_)):
        res += 1
        for i in range(len(limit_)):
          limit_[i] -= a[i]

    return res

  def findMaxForm(self, strs, chr, limit):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    arr = [[s.count(c) for c in chr] for s in strs]
    arr1 = sorted(arr, key=lambda s: -min(l - ss for ss, l in zip(s, limit)))
    arr2 = sorted(arr, key=lambda s: min(s))
    res = max(self.getMax(arr1, limit), self.getMax(arr2, limit))

    return res

print(Solution().findMaxForm(["102", "00021", "111001", "100", "0", "2", '22'], ['0', '1', '2'], [5, 3, 4]))