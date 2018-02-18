
def maxLength(a, k):
  num = 0
  for l in range(1, len(a)):
    for i in range(len(a) - l + 1):
      if sum(a[i:i + l]) <= k:
        num = l
        break

      if i == len(a) - l:
        return num

  return num

print(maxLength([
  1, 2, 3, 7, 8, 3, 2, 1, 1, 1
], 8))