from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairs = sorted(weights[i] + weights[i + 1] for i in range(len(weights) - 1))
        return sum(pairs[len(pairs) - (k - 1):]) - sum(pairs[:k - 1])
