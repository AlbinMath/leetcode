from collections import defaultdict
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry

    def reset(self, x: int):
        self.parent[x] = x

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Group meetings by timestamp
        time_groups = defaultdict(list)
        for x, y, t in meetings:
            time_groups[t].append((x, y))

        dsu = DSU(n)
        # Person 0 shares secret with firstPerson at time 0
        dsu.union(0, firstPerson)

        for t in sorted(time_groups.keys()):
            current_meetings = time_groups[t]
            people = set()

            # 1. Connect people meeting at this timestamp
            for x, y in current_meetings:
                dsu.union(x, y)
                people.add(x)
                people.add(y)

            # 2. Reset those who did not receive the secret from 0
            for p in people:
                if not dsu.connected(p, 0):
                    dsu.reset(p)

        # 3. Collect all individuals who know the secret
        return [i for i in range(n) if dsu.connected(i, 0)]
