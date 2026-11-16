class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()
        best = 0

        def dfs(pos: int) -> None:
            nonlocal best
            if len(seen) + (n - pos) <= best:
                return  # even one character per piece can't beat best
            if pos == n:
                best = len(seen)
                return
            for end in range(pos + 1, n + 1):
                piece = s[pos:end]
                if piece in seen:
                    continue
                seen.add(piece)
                dfs(end)
                seen.remove(piece)

        dfs(0)
        return best
