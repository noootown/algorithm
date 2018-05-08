# https://leetcode.com/problems/find-right-interval/description/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import bisect
class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        s = sorted([(v.start, i) for i, v in enumerate(intervals)])
        ans = []
        for i in intervals:
            p = bisect.bisect_left(s, (i.end, ))
            ans.append(-1 if p == len(s) else s[p][1])
        return ans
