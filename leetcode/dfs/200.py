# https://leetcode.com/problems/number-of-islands/description/
# http://bit.ly/2wspoYN
class Solution:
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def sink(i, j):
      if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
        grid[i][j] = '0'
        for i_, j_ in zip((i, i, i - 1, i + 1), (j - 1, j + 1, j, j)):
          sink(i_, j_)
        return 1
      return 0

    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))