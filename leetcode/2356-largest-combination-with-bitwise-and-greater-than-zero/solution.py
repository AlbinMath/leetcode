from typing import List


class Solution:

  def largestCombination(self, candidates: List[int]) -> int:
    return max(
        sum((num >> bit) & 1 for num in candidates) for bit in range(24)
    )
