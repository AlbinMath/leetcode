from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count = Counter(s)

        if max(count.values()) > (n + 1) // 2:
            return ""

        res = [''] * n
        idx = 0

        # most frequent first
        for ch, freq in count.most_common():
            for _ in range(freq):
                res[idx] = ch
                idx += 2
                if idx >= n:
                    idx = 1   # wrap to odd positions

        return ''.join(res)
