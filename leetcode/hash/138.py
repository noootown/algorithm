# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# http://bit.ly/2FxTPMv

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
from collections import defaultdict
def factory():
  return RandomListNode(0)

class Solution:
  # @param head, a RandomListNode
  # @return a RandomListNode
  def copyRandomList(self, head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    if not head:
      return None
    temp = head
    node_map = defaultdict(factory)
    node_map[None] = None # avoid None as key to generate a RandomListNode
    while temp:
      node_map[temp].label = temp.label
      node_map[temp].next = node_map[temp.next]
      node_map[temp].random = node_map[temp.random]
      temp = temp.next
    del node_map[None]
    return node_map[head]
