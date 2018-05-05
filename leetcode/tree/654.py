# https://leetcode.com/problems/maximum-binary-tree/description/
# top down
# http://bit.ly/2JQtGLq
# bottom up
# http://bit.ly/2JPcTrX

# top down
class Solution:
  def constructMaximumBinaryTree(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    dummy = TreeNode(None)

    def d(root, nums):
      if not nums:
        return
      i = nums.index(max(nums))
      root.val = nums[i]
      if nums[:i]:
        root.left = TreeNode(None)
        d(root.left, nums[:i])
      if nums[i + 1:]:
        root.right = TreeNode(None)
        d(root.right, nums[i + 1:])

    d(dummy, nums)
    return dummy

# bottom up (faster)
class Solution:
  def constructMaximumBinaryTree(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums:
      return None
    node_stack = []
    for num in nums:
      curNode = TreeNode(num)
      while node_stack and num > node_stack[-1].val:
        curNode.left = node_stack.pop()
      if node_stack:
        node_stack[-1].right = curNode
      node_stack.append(curNode)
    return node_stack[0]