from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = sorted(Counter(s).values(), reverse=True)
        limit = freqs[0]
        deletions = 0

        for f in freqs:
            keep = min(f, limit)
            deletions += f - keep
            limit = max(0, keep - 1)

        return deletions
