from typing import List

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        g = [set() for _ in range(n + 1)]
        deg = [0] * (n + 1)

        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            deg[u] += 1
            deg[v] += 1

        odd = [i for i in range(1, n + 1) if deg[i] % 2]

        if not odd:
            return True
        if len(odd) == 2:
            a, b = odd
            if b not in g[a]:
                return True
            for x in range(1, n + 1):
                if x != a and x != b and x not in g[a] and x not in g[b]:
                    return True
            return False
        if len(odd) == 4:
            a, b, c, d = odd
            return ((b not in g[a] and d not in g[c]) or
                    (c not in g[a] and d not in g[b]) or
                    (d not in g[a] and c not in g[b]))
        return False
