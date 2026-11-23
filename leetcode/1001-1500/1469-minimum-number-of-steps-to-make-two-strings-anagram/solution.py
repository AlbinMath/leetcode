from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = Counter(t) - Counter(s)  # keeps only positive surpluses in t
        return sum(diff.values())
