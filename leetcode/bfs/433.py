# https://leetcode.com/problems/minimum-genetic-mutation/

class Solution(object):
  def minMutation(self, start, end, bank):
    """
    :type start: str
    :type end: str
    :type bank: List[str]
    :rtype: int
    """
    front, back, bank_set, result = { start }, { end }, set(bank), 0
    def distance(str1, str2):
      return sum(s1 != s2 for s1, s2 in zip(str1, str2))

    while 1:
      front_ = set()
      for s in front:
        for b in bank_set:
          if distance(s, b) == 1:
            front_.add(b)

      result += 1
      bank_set -= front_
      if len(front_) == 0:
        return -1

      if len(front_ & back) != 0:
        return result

      front = front_


assert Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2
assert Solution().minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]) == 3
assert Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
assert Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTC"]) == -1
