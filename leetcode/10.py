# https://leetcode.com/problems/regular-expression-matching/description/
# http://bit.ly/2EBeXWq

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        table = [[False for _ in range(len(p) + 1)] for __ in range(len(s) + 1)]
        table[-1][-1] = True

        for s_ in range(len(s), -1, -1):
            for p_ in range(len(p) - 1, -1, -1):
                fm = s_ != len(s) and (s[s_] == p[p_] or p[p_] == '.')
                table[s_][p_] = p_ != len(p) - 1 and p[p_ + 1] == '*' and (table[s_][p_ + 2] or fm and table[s_ + 1][p_]) or \
                            fm and table[s_+1][p_+1]
        return table[0][0]

s = Solution()
s.isMatch("aab", "c*a*b")





