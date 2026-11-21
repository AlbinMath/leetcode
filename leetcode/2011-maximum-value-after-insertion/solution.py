class Solution:
    def maxValue(self, n: str, x: int) -> str:
        d = str(x)
        start = 1 if n[0] == '-' else 0

        for i in range(start, len(n)):
            if start == 0 and n[i] < d:
                return n[:i] + d + n[i:]
            if start == 1 and n[i] > d:
                return n[:i] + d + n[i:]

        return n + d
