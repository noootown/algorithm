class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends:
            return -1

        qs = set(deadends)
        qs.add('0000')

        q = [['0000']]
        k = 0
        while 1:
            subq = []
            for s in q[0]:
                if s == target:
                    return k
                subq += [s[:i] + str((int(s[i]) + 1) % 10) + s[i+1:] for i in range(4) if ss not in qs]
                subq += [s[:i] + str((int(s[i]) - 1) % 10) + s[i+1:] for i in range(4) if ss not in qs]
            qs = qs & set(subq)
            q.append(subq)
            del q[0]
            k += 1
            if not q[0]:
                return -1

s = Solution()
print(s.openLock(["0201","0101","0102","1212","2002"], "0202"))
