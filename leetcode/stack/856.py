# https://leetcode.com/problems/score-of-parentheses/description/

class Solution:
  def scoreOfParentheses(self, S):
    """
    :type S: str
    :rtype: int
    """
    stack = []
    for ele in S:
      if ele == '(':
        stack.append(ele)
      elif ele == ')':
        local_sum = 0
        while 1:
          eleb = stack.pop()
          if eleb == '(':
            if local_sum != 0:
              local_sum *= 2
            else:
              local_sum = 1
            break
          else:
            local_sum += eleb
        stack.append(local_sum)
    return sum(stack)

class Solution:
  def scoreOfParentheses(self, S):
    """
    :type S: str
    :rtype: int
    """
    stack, res = [], 0
    for i in range(len(S)):
      if S[i] == "(":
        stack.append("(")
      else:
        stack.pop()
        if S[i - 1] == "(":
          res += 2 ** len(stack)
    return res
