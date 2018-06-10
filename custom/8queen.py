# dim = 8
# stack = []
#
# def dfs(row):
#   if row == dim:
#     for i in range(dim):
#       print('x'*stack[i] + 'o' + 'x'*(dim-stack[i]-1))
#     return True
#
#   for i in range(dim):
#     if all(i != s and row-j != abs(i-s) for j, s in enumerate(stack)):
#       stack.append(i)
#       if dfs(row + 1):
#         break
#       stack.pop()
#
#   return False
#
# dfs(0)

dim, stack = 8, []
nstate = [0] * dim

while len(stack) < dim:
  for i in range(nstate[len(stack)], dim):
    if all(i != s and len(stack)-j != abs(i-s) for j, s in enumerate(stack)):
      nstate[len(stack)] = i+1
      stack.append(i)
      break
  else:
    if stack:
      nstate[len(stack)] = 0
      stack.pop()

for i in range(dim):
  print('x'*stack[i] + 'o' + 'x'*(dim-stack[i]-1))
