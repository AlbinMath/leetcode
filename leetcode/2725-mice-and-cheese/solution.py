from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diffs = sorted((a - b for a, b in zip(reward1, reward2)), reverse=True)
        return sum(reward2) + sum(diffs[:k])
