# https://leetcode.com/problems/reconstruct-itinerary/description/
# http://bit.ly/2L1OMb8

from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets, route = defaultdict(list), []
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]