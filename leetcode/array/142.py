# https://leetcode.com/problems/linked-list-cycle-ii/description/
# http://bit.ly/2GLCK6i
# similar problem as 287
# https://leetcode.com/problems/find-the-duplicate-number/description/

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
      fast = head.next
      slow = head
      while fast is not slow:
        fast = fast.next.next
        slow = slow.next
    except:
      # if there is an exception, we reach the end and there is no cycle
      return None

      # since fast starts at head.next, we need to move slow one step forward
    slow = slow.next
    while head is not slow:
      head = head.next
      slow = slow.next

    return head