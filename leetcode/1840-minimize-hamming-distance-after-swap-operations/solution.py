from collections import defaultdict, Counter
from typing import List

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        # 1. Group indices into components
        for u, v in allowedSwaps:
            union(u, v)

        # 2. Count frequencies of source elements in each component
        component_counts = defaultdict(Counter)
        for i in range(n):
            root = find(i)
            component_counts[root][source[i]] += 1

        # 3. Match with target elements
        hamming_distance = 0
        for i in range(n):
            root = find(i)
            val = target[i]
            if component_counts[root][val] > 0:
                component_counts[root][val] -= 1
            else:
                hamming_distance += 1

        return hamming_distance
