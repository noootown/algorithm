# http://codeforces.com/contest/327/submission/4019241
n = int(input())
num = list(map(int, input().split()))

one, cur, lcs = 0, 0, 0
for i in num:
    if i == 0:
        cur += 1
        lcs = max(lcs, cur)
    else:
        one += 1
        cur = max(cur - 1, 0)

print(one + lcs if one != n else one - 1)
