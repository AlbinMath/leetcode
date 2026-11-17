from functools import reduce
import operator
from typing import List


class Solution:

  def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
    xor1 = reduce(operator.xor, arr1, 0)
    xor2 = reduce(operator.xor, arr2, 0)
    return xor1 & xor2
