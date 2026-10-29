class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        parent = list(range(n))
        count = n  # Number of disjoint components

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
                count -= 1

        for i in range(0, len(row), 2):
            couple1 = row[i] // 2
            couple2 = row[i + 1] // 2
            union(couple1, couple2)

        return n - count
