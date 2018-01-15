import math
n, m, a = [int(a) for a in input('').split(' ')]
print(int(math.ceil(n/a) * math.ceil(m/a)))
