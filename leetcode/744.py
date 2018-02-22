class Solution:
  def nextGreatestLetter(self, letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    return next((c for c in letters if c > target), letters[0])