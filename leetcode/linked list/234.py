# https://leetcode.com/problems/palindrome-linked-list/description/
# http://bit.ly/2wxqzGy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            rev, slow.next, slow = slow, rev, slow.next
        # CHECK odd
        if fast:
            slow = slow.next
        while slow:
            if slow.val != rev.val:
                return False
            slow, rev = slow.next, rev.next
        return True