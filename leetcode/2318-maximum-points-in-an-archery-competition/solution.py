from typing import List

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        best_score = -1
        best_mask = 0
        for mask in range(1 << 12):
            cost = 0
            score = 0
            for k in range(12):
                if mask >> k & 1:
                    cost += aliceArrows[k] + 1
                    score += k
            if cost <= numArrows and score > best_score:
                best_score = score
                best_mask = mask

        bob = [0] * 12
        used = 0
        for k in range(12):
            if best_mask >> k & 1:
                bob[k] = aliceArrows[k] + 1
                used += bob[k]
        bob[0] += numArrows - used  # leftover arrows, harmless on section 0
        return bob
