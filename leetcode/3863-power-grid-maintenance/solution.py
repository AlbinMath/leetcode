import heapq
from collections import defaultdict
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        # Group all stations into their component lists
        comp_nodes = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            comp_nodes[root].append(i)

        # Convert each component's list into a min-heap
        heaps = {}
        for root, nodes in comp_nodes.items():
            heapq.heapify(nodes)
            heaps[root] = nodes

        is_online = [True] * (c + 1)
        ans = []

        for q_type, x in queries:
            if q_type == 1:
                if is_online[x]:
                    ans.append(x)
                else:
                    root = dsu.find(x)
                    hp = heaps[root]

                    # Lazily remove offline stations from the top of the heap
                    while hp and not is_online[hp[0]]:
                        heapq.heappop(hp)

                    ans.append(hp[0] if hp else -1)
            else:
                is_online[x] = False

        return ans
