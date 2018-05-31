# https://leetcode.com/problems/word-ladder/description/
# http://bit.ly/2KQBZat

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        length, front, back, ws = 2, {beginWord}, {endWord}, set(wordList)
        if endWord not in ws:
            return 0
        while front:
            front = ws & (set(word[:index] + ch + word[index+1:] for word in front
                                for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                return length
            length += 1
            if len(front) > len(back):
                front, back = back, front
            ws -= front
        return 0