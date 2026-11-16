from typing import List

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        divs = [d for d in range(1, n + 1) if n % d == 0]
        best = [float('inf'), None]
        path = []

        def dfs(rem: int, left: int, start: int) -> None:
            if left == 1:
                # last factor is rem itself; it must not be below the previous one
                if path and rem < divs[start]:
                    return
                path.append(rem)
                diff = path[-1] - path[0]
                if diff < best[0]:
                    best[0] = diff
                    best[1] = path[:]
                path.pop()
                return
            for idx in range(start, len(divs)):
                d = divs[idx]
                if d ** left > rem:
                    break  # remaining factors are all >= d, so the product would exceed rem
                if rem % d:
                    continue
                path.append(d)
                dfs(rem // d, left - 1, idx)
                path.pop()

        dfs(n, k, 0)
        return best[1]
