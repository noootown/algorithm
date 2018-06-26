# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Node:
  def __init__(self, ch):
    self.ch = ch
    self.isEnd = False
    self.next = []

class Trie:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = Node('root')

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    ptr = self.root
    for i, w in enumerate(word):
      for ptr_ in ptr.next:
        if ptr_.ch == w:
          ptr = ptr_
          break
      else:
        for wp in range(i, len(word)):
          ptr.next.append(Node(word[wp]))
          ptr = ptr.next[-1]
        break
    ptr.isEnd = True

  def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    ptr = self.root
    for w in word:
      for ptr_ in ptr.next:
        if ptr_.ch == w:
          ptr = ptr_
          break
      else:
        return False
    return ptr.isEnd

  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    ptr = self.root
    for w in prefix:
      for ptr_ in ptr.next:
        if ptr_.ch == w:
          ptr = ptr_
          break
      else:
        return False
    return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
print(trie.search("bpp"))
trie.insert("b")
print(trie.search("bpp"))
print(trie.search("b"))

class Trie:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = {}
    self.end = -1

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """

    curNode = self.root
    for c in word:
      if not c in curNode:
        curNode[c] = {}
      curNode = curNode[c]
    curNode[self.end] = True

  def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    curNode = self.root
    for c in word:
      if not c in curNode:
        return False
      curNode = curNode[c]
    return self.end in curNode

  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    curNode = self.root
    for c in prefix:
      if not c in curNode:
        return False
      curNode = curNode[c]
    return True
