# https://leetcode.com/problems/sliding-puzzle/description/
# http://bit.ly/2GZenhx

from collections import deque

class Solution:
  def slidingPuzzle(self, board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    board_ans = [[1,2,3], [4,5,0]]

    if all(n1 == n2 for row1, row2 in zip(board, board_ans) for n1, n2 in zip(row1, row2)):
      return 0

    def hash(board):
      return "".join([str(n) for row in board for n in row])

    state, ans, cond = hash(board), hash([[1,2,3], [4,5,0]]), [
      (lambda x: x - 1 >= 0 and x != 3, -1),
      (lambda x: x - 3 >= 0, -3),
      (lambda x: x + 1 < 6 and x != 2, 1),
      (lambda x: x + 3 < 6, 3),
    ]
    s, q = {state}, deque([(state, 0)])
    while q:
      state, step = q.popleft()
      z = state.find('0')
      for c in cond:
        if c[0](z):
          state_ = [s for s in state]
          state_[z], state_[z + c[1]] = state_[z + c[1]], state_[z]
          state_ = "".join(state_)
          if state_ == ans:
            return step + 1
          elif state_ not in s:
            s.add(state_)
            q.append((state_, step+1))
    return -1


