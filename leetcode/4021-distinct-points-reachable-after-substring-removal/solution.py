class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        px = [0] * (n + 1)
        py = [0] * (n + 1)
        for i, ch in enumerate(s):
            dx, dy = d[ch]
            px[i + 1] = px[i] + dx
            py[i + 1] = py[i] + dy

        X, Y = px[n], py[n]
        seen = set()
        for i in range(n - k + 1):
            seen.add((X - (px[i + k] - px[i]), Y - (py[i + k] - py[i])))
        return len(seen)
