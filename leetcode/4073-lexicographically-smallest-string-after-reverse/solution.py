class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        best = s[::-1]  # k = n (either side) gives the full reversal
        for k in range(1, n + 1):
            a = s[:k][::-1] + s[k:]            # reverse first k
            b = s[:n - k] + s[n - k:][::-1]    # reverse last k
            if a < best:
                best = a
            if b < best:
                best = b
        return best
