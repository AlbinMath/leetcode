from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        delta = [0] * n
        best = 0

        def dfs(i: int, chosen: int, nonzero: int) -> None:
            nonlocal best
            if chosen + (m - i) <= best:
                return  # even taking every remaining request can't beat best
            if i == m:
                if nonzero == 0:
                    best = chosen
                return

            f, t = requests[i]

            # take request i
            nz = nonzero
            if f != t:
                nz -= delta[f] != 0
                delta[f] -= 1
                nz += delta[f] != 0
                nz -= delta[t] != 0
                delta[t] += 1
                nz += delta[t] != 0
            dfs(i + 1, chosen + 1, nz)
            if f != t:
                delta[f] += 1
                delta[t] -= 1

            # skip request i
            dfs(i + 1, chosen, nonzero)

        dfs(0, 0, 0)
        return best
