from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        freqs = sorted(Counter(arr).values())
        unique = len(freqs)
        for f in freqs:
            if k >= f:
                k -= f
                unique -= 1
            else:
                break
        return unique
