# https://leetcode.com/problems/sort-list/description/
# http://bit.ly/2svAfvB

class Solution:
  def merge(self, h1, h2):
    dummy = tail = ListNode(None)
    while h1 and h2:
      if h1.val < h2.val:
        tail.next, tail, h1 = h1, h1, h1.next
      else:
        tail.next, tail, h2 = h2, h2, h2.next

    tail.next = h1 or h2
    return dummy.next

  def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
      return head
    pre, fast, slow = None, head, head
    while fast and fast.next:
      pre, slow, fast = slow, slow.next, fast.next.next
    pre.next = None
    return self.merge(self.sortList(head), self.sortList(slow))