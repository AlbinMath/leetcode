from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int],
                              numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        used = defaultdict(int)
        total = taken = 0
        for v, l in items:
            if taken == numWanted:
                break
            if used[l] < useLimit:
                used[l] += 1
                total += v
                taken += 1
        return total
