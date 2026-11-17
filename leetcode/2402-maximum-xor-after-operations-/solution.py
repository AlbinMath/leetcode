from functools import reduce
import operator
from typing import List


class Solution:

  def maximumXOR(self, nums: List[int]) -> int:
    return reduce(operator.or_, nums, 0)
