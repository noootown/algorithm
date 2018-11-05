# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
# http://bit.ly/2Jp5QGD

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  # @param two ListNodes
  # @return the intersected ListNode
  def getIntersectionNode(self, headA, headB):
    if headA is None or headB is None:
      return None

    pa, pb = headA, headB  # 2 pointers

    while pa is not pb:
      # if either pointer hits the end, switch head and continue the second traversal,
      # if not hit the end, just move on to next
      pa = headB if pa is None else pa.next
      pb = headA if pb is None else pb.next

    return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None

    # the idea is if you switch head, the possible difference between length would be countered.
    # On the second traversal, they either hit or miss.
    # if they meet, pa or pb would be the node we are looking for,
    # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None

# O(n) memory
class Solution:
  # @param two ListNodes
  # @return the intersected ListNode
  def getIntersectionNode(self, headA, headB):
    if headA is None or headB is None:
      return None

    pa, pb, mem = headA, headB, set()

    while pa:
      mem.add(pa)
      pa = pa.next

    while pb:
      if pb in mem:
        return pb
      pb = pb.next
