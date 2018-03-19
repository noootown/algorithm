# https://leetcode.com/problems/my-calendar-i/description/
# https://leetcode.com/problems/my-calendar-i/solution/

class Node:
  def __init__(self, start, end):
    self.start = start
    self.end = end
    self.right = None
    self.left = None

  def insert(self, start, end):
    if start >= self.end:
      if self.right:
        return self.right.insert(start, end)
      else:
        self.right = Node(start, end)
        return True
    elif end <= self.start:
      if self.left:
        return self.left.insert(start, end)
      else:
        self.left = Node(start, end)
        return True
    else:
      return False

class MyCalendar:
  def __init__(self):
    self.calendar = None

  def book(self, start, end):
    """
    :type start: int
    :type end: int
    :rtype: bool
    """
    if self.calendar is None:
      self.calendar = Node(start, end)
      return True
    else:
      return self.calendar.insert(start, end)
