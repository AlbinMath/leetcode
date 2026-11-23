from collections import defaultdict
from typing import List

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append((v, 0))  # u -> v: no reversal needed from u
            graph[v].append((u, 1))  # v -> u: reversing this edge is needed

        answer = [0] * n

        # First DFS: calculate reversals needed when starting at node 0
        def dfs(node, parent):
            for nei, cost in graph[node]:
                if nei == parent:
                    continue

                answer[0] += cost
                dfs(nei, node)

        dfs(0, -1)

        # Second DFS: calculate answers for all other starting nodes
        def reroot(node, parent):
            for nei, cost in graph[node]:
                if nei == parent:
                    continue

                if cost == 0:
                    answer[nei] = answer[node] + 1
                else:
                    answer[nei] = answer[node] - 1

                reroot(nei, node)

        reroot(0, -1)
        return answer
