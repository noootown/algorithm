# https://leetcode.com/problems/linked-list-cycle-ii/description/
# http://bit.ly/2GLCK6i
# similar problem as 287
# https://leetcode.com/problems/find-the-duplicate-number/description/
# https://www.youtube.com/watch?v=KjwoQ-WhW3g

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    try:
      slow, fast = head, head.next
      while fast is not slow:
        slow, fast = slow.next, fast.next.next
    except:
      # if there is an exception, we reach the end and there is no cycle
      return None

    # since fast starts at head.next, we need to move slow one step forward
    slow = slow.next
    while head is not slow:
      slow, head = slow.next, head.next

    return head

class Solution(object):
  def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
      return None

    current = head
    dict = {}

    while current:
      if current not in dict:
        dict[current] = current
      else:
        return dict[current]
      current = current.next

    return None