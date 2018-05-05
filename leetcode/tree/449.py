# https://leetcode.com/problems/serialize-and-deserialize-bst/description/
# http://bit.ly/2JSDRij

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """

    def preorder(node):
      if node:
        vals.append(str(node.val))
        preorder(node.left)
        preorder(node.right)

    vals = []
    preorder(root)
    return ' '.join(vals)

  def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    preorder = map(int, data.split())
    inorder = sorted(preorder)
    return self.buildTree(preorder, inorder)

  def buildTree(self, preorder, inorder):
    def build(stop):
      if inorder and inorder[-1] != stop:
        root = TreeNode(preorder.pop())
        root.left = build(root.val)
        inorder.pop()
        root.right = build(stop)
        return root

    preorder.reverse()
    inorder.reverse()
    return build(None)


    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))
