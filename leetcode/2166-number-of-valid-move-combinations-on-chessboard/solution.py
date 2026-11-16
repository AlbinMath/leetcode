from typing import List

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        ROOK = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        BISHOP = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        dirs = {"rook": ROOK, "bishop": BISHOP, "queen": ROOK + BISHOP}

        n = len(pieces)
        moves = []
        for k in range(n):
            r, c = positions[k]
            opts = [(r, c, 0, 0, 0)]  # stay: (r, c, dr, dc, steps)
            for dr, dc in dirs[pieces[k]]:
                for s in range(1, 8):
                    nr, nc = r + dr * s, c + dc * s
                    if not (1 <= nr <= 8 and 1 <= nc <= 8):
                        break
                    opts.append((r, c, dr, dc, s))
            moves.append(opts)

        def conflict(a, b) -> bool:
            ra, ca, dra, dca, sa = a
            rb, cb, drb, dcb, sb = b
            for t in range(max(sa, sb) + 1):
                ta, tb = min(t, sa), min(t, sb)
                if (ra + dra * ta == rb + drb * tb and
                        ca + dca * ta == cb + dcb * tb):
                    return True
            return False

        chosen = []

        def dfs(k: int) -> int:
            if k == n:
                return 1
            total = 0
            for m in moves[k]:
                if all(not conflict(m, o) for o in chosen):
                    chosen.append(m)
                    total += dfs(k + 1)
                    chosen.pop()
            return total

        return dfs(0)
