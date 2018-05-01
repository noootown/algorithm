# https://leetcode.com/problems/top-k-frequent-words/description/
# http://bit.ly/2FxtGx2

from collections import Counter
import heapq
import functools

@functools.total_ordering
class Element:
  def __init__(self, name, count):
    self.count = count
    self.name = name

  def __lt__(self, other):
    if self.count == other.count:
      return self.name > other.name
    return self.count < other.count

  def __eq__(self, other):
    return self.count == other.count and self.name == other.name


class Solution:
  def topKFrequent(self, words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    s = Counter(words)
    freq = []
    heapq.heapify(freq)
    for ss in s.items():
      heapq.heappush(freq, Element(*ss))
      if len(freq) > k:
        heapq.heappop(freq)

    return [heapq.heappop(freq).name for _ in range(k)][::-1]

s = Solution()
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))