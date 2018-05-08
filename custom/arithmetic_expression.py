# input list
# output the possible outcome by using +, -, * operations
arr = [1,2,3]

N = len(arr)
dp = [[set() for _ in range(N)] for _ in range(N)]
for j in range(N):
  dp[j][j].add(arr[j])

# with parenthesis
for i in range(1, N):
  for j in range(0, N-i):
    if i == 1:
      for l in dp[j][j]:
        for r in dp[j+i][j+i]:
          dp[j][j+i].add(l + r)
          dp[j][j+i].add(l - r)
          dp[j][j+i].add(l * r)
    else:
      for l in dp[j][j]:
        for r in dp[j+1][j+i]:
          dp[j][j+i].add(l + r)
          dp[j][j+i].add(l - r)
          dp[j][j+i].add(l * r)
      for l in dp[j][j+i-1]:
        for r in dp[j+i][j+i]:
          dp[j][j+i].add(l + r)
          dp[j][j+i].add(l - r)
          dp[j][j+i].add(l * r)

print(len(dp[0][-1]))
