from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        return sum(1 if count % 2 == 1 else 2 for count in freq.values())
