from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        odd = sum(v % 2 for v in Counter(s).values())
        return odd <= k
