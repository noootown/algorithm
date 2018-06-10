# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
# http://bit.ly/2HbJOoY

from heapq import heappop, heappush, merge
from itertools import islice
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        return [suv[1:] for suv in islice(merge(*map(lambda u: ([u+v, u, v] for v in nums2), nums1)), k)]

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(heap, (nums1[i] + nums2[j], i, j))

        push(0, 0)
        res = []
        while heap and len(res) < k:
            _, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return res