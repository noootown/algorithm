# https://leetcode.com/problems/number-of-atoms/description/
from collections import defaultdict
import re

class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        p, stk, d = 0, [], defaultdict(int)
        while p < len(formula):
            if formula[p] in ('(', ')'):
                stk.append(formula[p])
                p+=1
            elif 'A' <= formula[p] <= 'Z':
                if p+1 < len(formula) and 'a' <= formula[p+1] <= 'z':
                    stk.append([formula[p:p+2], 1])
                    p+=2
                else:
                    stk.append([formula[p], 1])
                    p+=1
            elif '0' <= formula[p] <= '9':
                i = 1
                while p+i < len(formula) and '0' <= formula[p+i] <= '9':
                    i+=1
                num = int(formula[p:p+i])
                p += i
                if stk[-1] == ')':
                    stk.pop()
                    t = []
                    while stk[-1] != '(':
                        s = stk.pop()
                        s[1] *= num
                        t.append(s)
                    stk.pop()
                    stk += t
                else:
                    s = stk.pop()
                    s[1] *= num
                    stk.append(s)
        for k, v in stk:
            d[k] += v
        ans = ''
        for k in sorted(d.keys()):
            ans += '%s%d' % (k, d[k]) if d[k] > 1 else k
        return ans

class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        d = defaultdict(int)
        def p(m):
            num = int(m.group(2))
            return ''.join('%s%d' % (c, int(n) * num if n else num)
                           for c, n in re.findall('([A-Z][a-z]?)(\d*)', m.group(1)))
        while '(' in formula:
            formula = re.sub('\((\w+)\)(\d+)', p, formula)
        for k, v in re.findall('([A-Z][a-z]?)(\d*)', formula):
            d[k] += 1 if not v else int(v)
        return ''.join(['%s%d' % (k, d[k]) if d[k] > 1 else k for k in sorted(d.keys())])
