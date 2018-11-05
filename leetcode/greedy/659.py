# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
# https://leetcode.com/submissions/detail/156845068/

class Solution:
  def isPossible(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    s, K = set(), 3
    for n in nums:
      for k in range(1, K + 1):
        ele = (n - 1, k)
        if ele in s:
          s.remove(ele)
          s.add((n, k + 1 if k < K else K))
          break
      else:
        s.add((n, 1))

    for ss in s:
      if ss[1] < K:
        return False
    return True

from itertools import groupby
from collections import deque

class Solution:
  def isPossible(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    arr = [(c, len(list(g))) for c, g in groupby(nums)]
    print(arr)

    prev, prevCount = arr[0]
    starts = deque([(prev, prevCount)])

    for i in range(1, len(arr)):
      curr, currCount = arr[i]
      if curr != prev + 1:
        if prev < starts[-1][0] + 2:
          return False
        starts = deque([(curr, currCount)])
      elif currCount > prevCount:
        starts.append((curr, currCount - prevCount))
      elif currCount < prevCount:
        diff = prevCount - currCount
        while diff > 0:
          a, b = starts.popleft()
          if prev - a < 2:
            return False
          elif b > diff:
            starts.appendleft((a, b - diff))
          diff -= b

      prev, prevCount = curr, currCount

    if arr[-1][0] < starts[-1][0] + 2:
      return False
    return True

from collections import Counter

class Solution:
  def isPossible(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    left, end = Counter(nums), Counter()

    for i in nums:
      if not left[i]:
        continue
      left[i] -= 1
      if end[i - 1] > 0:
        end[i - 1] -= 1
        end[i] += 1
      elif left[i + 1] and left[i + 2]:
        left[i + 1] -= 1
        left[i + 2] -= 1
        end[i + 2] += 1
      else:
        return False
    return True
