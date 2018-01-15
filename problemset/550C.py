s = input()
candidate = [str(x) for x in range(0, 1000, 8)]

def isContain(str, substr):
    d = {i:ss for i, ss in enumerate(substr)}
    ptr = 0
    for ss in str:
        if d[ptr] == ss:
            ptr += 1
        if ptr == len(substr):
            return True
    return False

for ss in candidate:
    if isContain(s, ss):
        print('YES')
        print(ss)
        exit()
print('NO')
