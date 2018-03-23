# https://leetcode.com/problems/next-permutation/description/
# http://bit.ly/2IHKyEc
# http://bit.ly/2IFqrXl

class Solution:
  def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    return self.buildrecurtree({num: i for i, num in enumerate(inorder)}, preorder, inorder, 0, 0, len(inorder))

  def buildrecurtree(self, lookup, preorder, inorder, pre_start, in_start, in_end):
    if in_start == in_end:
      return None
    node = TreeNode(preorder[pre_start])
    i = lookup[preorder[pre_start]]
    node.left = self.buildrecurtree(lookup, preorder, inorder, pre_start + 1, in_start, i)
    node.right = self.buildrecurtree(lookup, preorder, inorder, pre_start + 1 + i - in_start, i + 1, in_end)
    return node
