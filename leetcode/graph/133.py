# https://leetcode.com/problems/clone-graph/description/
# http://bit.ly/2rAsxkw
# http://bit.ly/2rDvbpr

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

from collections import deque

# BFS
class Solution:
  # @param node, a undirected graph node
  # @return a undirected graph node
  def cloneGraph(self, node):
    if not node:
      return
    dic = {node: UndirectedGraphNode(node.label)}
    queue = deque([node])
    while queue:
      node = queue.popleft()
      for neighbor in node.neighbors:
        if neighbor not in dic: # neighbor is not visited
          dic[neighbor] = UndirectedGraphNode(neighbor.label)
          queue.append(neighbor)
        dic[node].neighbors.append(dic[neighbor])
    return dic[node]

# DFS
class Solution:
  # @param node, a undirected graph node
  # @return a undirected graph node
  def cloneGraph(self, node):
    if not node:
      return
    nodeCopy = UndirectedGraphNode(node.label)
    dic = {node: nodeCopy}
    stack = [node]
    while stack:
      node = stack.pop()
      for neighbor in node.neighbors:
        if neighbor not in dic:  # neighbor is not visited
          dic[neighbor] = UndirectedGraphNode(neighbor.label)
          stack.append(neighbor)
        dic[node].neighbors.append(dic[neighbor])
    return nodeCopy

# DFS
class Solution:
  # @param node, a undirected graph node
  # @return a undirected graph node

  def cloneGraph(self, node):
    memo = {}
    def clone(node):
      if node not in memo:
        memo[node] = UndirectedGraphNode(node.label)
        memo[node].neighbors = [clone(n) for n in  node.neighbors]
      return memo[node]
    return node and clone(node)
