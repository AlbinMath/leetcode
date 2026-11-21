class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        rows = max(len(w) for w in words)

        res = []
        for i in range(rows):
            line = ''.join(w[i] if i < len(w) else ' ' for w in words)
            res.append(line.rstrip())

        return res
