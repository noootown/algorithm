str = input()
ptr = 0
m = {
    0:'h',
    1:'e',
    2:'l',
    3:'l',
    4:'o',
    5:'#',
}
for i in str:
    if i == m[ptr]:
        ptr += 1

print('YES' if ptr == 5 else 'NO')

