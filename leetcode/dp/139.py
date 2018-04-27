# https://leetcode.com/problems/word-break/description/
# http://bit.ly/2HP6UWX

import functools

# ans 1
# 76 ms
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok = [True]
        for i in range(1, len(s) + 1):
            ok.append(any(ok[j] and s[j:i] in wordDict for j in range(i)))
        return ok[-1]

# ans2
# with decorator 36ms
# without decorator TLE
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # this decorator is amazing!!!
        @functools.lru_cache(maxsize=None)
        def can_decode(i):
            return i == len(s) or next((True for w in wordDict if s.startswith(w, i) and can_decode(i + len(w))), False)

        return can_decode(0)
