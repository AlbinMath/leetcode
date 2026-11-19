from typing import List
import heapq

class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])

        # Step 1: top 3 per row
        cand = []
        for r in range(m):
            for v, c in heapq.nlargest(3, ((board[r][c], c) for c in range(n))):
                cand.append((v, r, c))

        # Step 2: among those, top 3 per column
        by_col = [[] for _ in range(n)]
        for v, r, c in cand:
            by_col[c].append((v, r))
        pts = []
        for c in range(n):
            for v, r in heapq.nlargest(3, by_col[c]):
                pts.append((v, r, c))

        pts.sort(reverse=True)
        k = len(pts)  # at most 3 * min(m, n) <= 1500

        best = float('-inf')
        for a in range(k):
            v1, r1, c1 = pts[a]
            if v1 + pts[0][0] * 0 + 0 < 0 and best > float('-inf') and v1 * 3 < best:
                break  # even three copies of the largest remaining can't beat best
            for b in range(a + 1, k):
                v2, r2, c2 = pts[b]
                if r2 == r1 or c2 == c1:
                    continue
                if v1 + v2 + v2 < best:
                    break  # third value <= v2
                for d in range(b + 1, k):
                    v3, r3, c3 = pts[d]
                    if r3 == r1 or r3 == r2 or c3 == c1 or c3 == c2:
                        continue
                    s = v1 + v2 + v3
                    if s > best:
                        best = s
                    break  # later d have smaller values
        return best
