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

    def union(self, x: int, y: int) -> int:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.size[rx] < self.size[ry]:
                rx, ry = ry, rx
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]
        return self.size[rx]


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        dsu = DSU(n)
        active = [False] * n

        # Process indices ordered by value descending
        indices = sorted(range(n), key=lambda i: nums[i], reverse=True)

        for i in indices:
            active[i] = True
            k = 1

            if i > 0 and active[i - 1]:
                k = dsu.union(i, i - 1)
            if i + 1 < n and active[i + 1]:
                k = dsu.union(i, i + 1)

            if nums[i] * k > threshold:
                return k

        return -1
