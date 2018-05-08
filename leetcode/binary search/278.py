# https://leetcode.com/problems/first-bad-version/description/
# http://bit.ly/2Io4fns

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

from bisect import bisect

class Solution(object):
  def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """

    class Wrap:
      def __getitem__(self, i):
        return isBadVersion(i)

    return bisect.bisect(Wrap(), False, 0, n)
