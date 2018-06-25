# https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
  def __init__(self, num = 0):
    self.child = {}
    self.num = num

class MapSum:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = TrieNode()

  def insert(self, key, val):
    """
    :type key: str
    :type val: int
    :rtype: void
    """
    ptr = self.root
    for k in key:
      if k in ptr.child:
        ptr = ptr.child[k]
      else:
        ptr.child[k] = TrieNode(0)
        ptr = ptr.child[k]
    ptr.num = val

  def sum(self, prefix):
    """
    :type prefix: str
    :rtype: int
    """
    ptr, s = self.root, 0
    for p in prefix:
      if p in ptr.child:
        ptr = ptr.child[p]
      else:
        return 0
    return self.dfs(ptr)

  def dfs(self, node):
    return sum(self.dfs(v) for v in node.child.values()) + node.num

obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("ap"))
obj.insert("app", 2)
print(obj.sum("ap"))
