class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        components = n

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            nonlocal components
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
                components -= 1

        for u, v in connections:
            union(u, v)

        return components - 1
