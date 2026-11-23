from collections import deque
from typing import List

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        bad = set(forbidden)
        limit = max(max(forbidden), x) + a + b

        visited = {(0, False)}
        q = deque([(0, False, 0)])  # (position, last jump was backward, jumps)
        while q:
            p, back, d = q.popleft()
            if p == x:
                return d

            f = p + a
            if f <= limit and f not in bad and (f, False) not in visited:
                visited.add((f, False))
                q.append((f, False, d + 1))

            if not back:
                g = p - b
                if g >= 0 and g not in bad and (g, True) not in visited:
                    visited.add((g, True))
                    q.append((g, True, d + 1))
        return -1
