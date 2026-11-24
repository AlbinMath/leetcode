from collections import defaultdict
from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        # 1. Connect indices
        for u, v in pairs:
            union(u, v)

        # 2. Group characters by component root
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(s[i])

        # 3. Sort characters in descending order to pop efficiently from the back
        for root in groups:
            groups[root].sort(reverse=True)

        # 4. Construct result
        res = []
        for i in range(n):
            res.append(groups[find(i)].pop())

        return "".join(res)
