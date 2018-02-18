# https://leetcode.com/problems/pyramid-transition-matrix/description/
# http://bit.ly/2BAcIQr

from collections import defaultdict
from itertools import product

class Solution(object):

  def pyramidTransition(self, bottom, allowed):
    f = defaultdict(lambda: defaultdict(list))
    for a, b, c in allowed: f[a][b].append(c)

    pyramid = lambda bottom: \
        len(bottom) == 1 or any(pyramid(i) for i in product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))))

    return pyramid(bottom)
