# http://codeforces.com/contest/476/submission/8195732
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

x = input()
p = x.count('+')
m = x.count('-')
x = input()
p_ = x.count('+')
m_ = x.count('-')
n = x.count('?')
a = p - p_
b = m - m_

if a < 0 or b < 0 or a + b != n:
    print(.0)
else:
    print(nCr(n, a)/(1 << n))
