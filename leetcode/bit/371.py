# https://leetcode.com/problems/sum-of-two-integers/description/
# http://bit.ly/2G0PiCB

class Solution:
  def getSum(self, a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    
    # mask to get last 32 bits
    mask = 0xFFFFFFFF
    while b != 0:
      # ^ get different bits and & gets double 1s, << moves carry
      a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)