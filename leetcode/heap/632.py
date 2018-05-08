# https://leetcode.com/problems/smallest-range/description/
# http://bit.ly/2JVSqlh

import heapq
from collections import defaultdict, deque

# my solution
class Solution:
  def smallestRange(self, nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    h = []
    heapq.heapify(h)

    for i, row in enumerate(nums):
      for num in row:
        heapq.heappush(h, (num, i))

    s = set(range(len(nums)))
    d = defaultdict(int)
    q = deque()
    min_, max_ = h[0][0], h[-1][0]
    while h:
      num, r = heapq.heappop(h)
      d[r] += 1
      if d[r] == 1:
        s.remove(r)
      q.append((num, r))
      if not s:
        while not s:
          nump, rp = q.popleft()
          d[rp] -= 1
          if d[rp] == 0:
            s.add(rp)
          if num - nump < max_ - min_:
            min_, max_ = nump, num
    return [min_, max_]

class Solution:
  def smallestRange(self, nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    pq = [(row[0], i, 0) for i, row in enumerate(nums)]
    heapq.heapify(pq)

    ans = -1e9, 1e9
    right = max(row[0] for row in nums)
    while pq:
      left, i, j = heapq.heappop(pq)
      if right - left < ans[1] - ans[0]:
        ans = left, right
      if j + 1 == len(nums[i]):
        return ans
      v = nums[i][j + 1]
      right = max(right, v)
      heapq.heappush(pq, (v, i, j + 1))

class Solution:
  def smallestRange(self, nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    k = len(nums)
    idx = [0] * k

    dic = defaultdict(list)

    for i in range(k):
      dic[nums[i][0]].append(i)

    mi, ma = min(dic.keys()), max(dic.keys())

    ret = (mi, ma)
    while True:
      for i in dic[mi]:
        idx[i] += 1
        if idx[i] == len(nums[i]):
          return ret
        dic[nums[i][idx[i]]].append(i)
      dic.pop(mi)
      mi, ma = min(dic.keys()), max(dic.keys())
      if ma - mi < ret[1] - ret[0]:
        ret = (mi, ma)