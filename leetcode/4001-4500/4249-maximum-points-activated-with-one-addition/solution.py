from collections import defaultdict
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

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
            if self.size[rx] < self.size[ry]:
                rx, ry = ry, rx
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]


class Solution:
    def maxActivated(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)

        # Map each coordinate to the index of the first point seen with that coordinate
        x_first = {}
        y_first = {}

        for i, (x, y) in enumerate(points):
            if x in x_first:
                dsu.union(i, x_first[x])
            else:
                x_first[x] = i

            if y in y_first:
                dsu.union(i, y_first[y])
            else:
                y_first[y] = i

        # Collect component sizes for all unique roots
        comp_sizes = [dsu.size[i] for i in range(n) if dsu.parent[i] == i]
        comp_sizes.sort(reverse=True)

        if len(comp_sizes) >= 2:
            return comp_sizes[0] + comp_sizes[1] + 1
        return comp_sizes[0] + 1
