# https://leetcode.com/problems/my-calendar-ii/description/

class MyCalendarTwo:
  def __init__(self):
    self.sbook = []
    self.dbook = []

  def book(self, start, end):
    """
    :type start: int
    :type end: int
    :rtype: bool
    """
    for s, e in self.dbook:
      if start < e and end > s:
        return False

    for s, e in self.sbook:
      if start < e and end > s:
        self.dbook.append((max(s, start), min(e, end)))

    self.sbook.append((start, end))

    return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
