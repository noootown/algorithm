# http://codeforces.com/contest/4/submission/9363077
d, sumTime = [int(a) for a in input().split()]
minMax, minT, maxT = [], 0, 0

for dd in range(d):
    a, b = input().split()
    minMax.append((int(a), int(b)))
    minT += int(a)
    maxT += int(b)

if minT > sumTime or sumTime > maxT:
    print('NO')
    exit()

sumTime -= minT
ans = []

for index, (mi, ma) in enumerate(minMax):
    add = min(sumTime, ma - mi)
    ans.append(mi + add)
    sumTime -= add

print('YES')
print(' '.join([str(a) for a in ans]))
