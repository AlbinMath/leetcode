from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        seen = set()
        ans = 0

        for i in range(n):
            if i in seen:
                continue

            stack = [i]
            seen.add(i)
            nodes = []

            while stack:
                u = stack.pop()
                nodes.append(u)
                for v in g[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)

            if all(len(g[u]) == len(nodes) - 1 for u in nodes):
                ans += 1

        return ans
