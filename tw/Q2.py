def findMutationDistance(start, end, bank):
  queue = [(start, 0)]

  def calDis(s1, s2):
    ptr = 0
    for s in range(8):
      ptr += (s1[s] == s2[s])
    return ptr == 7

  while 1:
    if queue[0][0] == end:
      return queue[0][1]

    pp = 0
    while pp < len(bank):
      if calDis(queue[0][0], bank[pp]):
        queue.append((bank[pp], queue[0][1] + 1))
        del bank[pp]
      pp += 1

    queue = queue[1:]
    if not queue:
      return -1

print(findMutationDistance('AAAAAAAA', 'GGAACTAA', [
  'GAAAAAAA',
  'AAGAAAAA',
  'AAAAGAAA',
  'GGAAAAAA',
  'GGAATAAA',
  'GGAATCAA',
  'GGAAGCAA',
  'GGAACTAA',
]))