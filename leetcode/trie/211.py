# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/

class TrieNode:
  def __init__(self):
    self.child = {}
    self.isEnd = False

class WordDictionary:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = TrieNode()

  def addWord(self, word):
    """
    Adds a word into the data structure.
    :type word: str
    :rtype: void
    """
    ptr = self.root
    for k in word:
      if k in ptr.child:
        ptr = ptr.child[k]
      else:
        ptr.child[k] = TrieNode()
        ptr = ptr.child[k]
    ptr.isEnd = True

  def search(self, word):
    """
    Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
    :type word: str
    :rtype: bool
    """
    return self.subsearch(self.root, word)
  def subsearch(self, node, word):
    if not word:
      return node.isEnd
    elif word[0] == '.':
      return any(self.subsearch(n, word[1:]) for n in node.child.values())
    elif word[0] in node.child:
      return self.subsearch(node.child[word[0]], word[1:])
    else:
      return False

obj = WordDictionary()
obj.addWord("a")
obj.addWord("ab")
print(obj.search("a"))
