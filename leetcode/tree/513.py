# https://leetcode.com/problems/find-bottom-left-tree-value/description/
# http://bit.ly/2JMQ3kY

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        for node in queue:
            queue += [n for n in [node.right, node.left] if n is not None]
        return node.val
