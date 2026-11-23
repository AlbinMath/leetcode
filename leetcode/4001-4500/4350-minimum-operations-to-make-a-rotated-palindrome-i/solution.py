class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        v = [ord(c) - 97 for c in s]
        best = float('inf')
        for r in range(n):
            t = v[r:] + v[:r]
            cost = r
            for i in range(n // 2):
                d = (t[i] - t[n - 1 - i]) % 26
                cost += min(d, 26 - d)
            best = min(best, cost)
        return best
