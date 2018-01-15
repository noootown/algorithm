m, s = [int(i) for i in input().split()]

def find(rev = False):
    if m == 1 and s == 0:
        return 0
    
    sum, result = s, ''
    for i in range(m):
        j = 1 if i == 0 else 0
        ok = False
        for v in range(j, 10) if rev else reversed(range(j, 10)):
            if (m - i - 1)*9 >= sum - v >= 0:
                 ok = True
                 sum -= v
                 result += str(v)
                 break
        if not ok:
            return -1
    return result

print(find(True), find(False))
