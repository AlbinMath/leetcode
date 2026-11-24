class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.count = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            self.count -= 1

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dsu = DSU(4 * n * n)

        def get_index(r: int, c: int, k: int) -> int:
            return (r * n + c) * 4 + k

        for r in range(n):
            for c in range(n):
                ch = grid[r][c]
                # 1. Connect within the current square
                if ch == ' ':
                    dsu.union(get_index(r, c, 0), get_index(r, c, 1))
                    dsu.union(get_index(r, c, 1), get_index(r, c, 2))
                    dsu.union(get_index(r, c, 2), get_index(r, c, 3))
                elif ch == '/':
                    dsu.union(get_index(r, c, 0), get_index(r, c, 3))
                    dsu.union(get_index(r, c, 1), get_index(r, c, 2))
                elif ch == '\\':
                    dsu.union(get_index(r, c, 0), get_index(r, c, 1))
                    dsu.union(get_index(r, c, 2), get_index(r, c, 3))

                # 2. Connect with adjacent squares
                # North-South connection
                if r + 1 < n:
                    dsu.union(get_index(r, c, 2), get_index(r + 1, c, 0))
                # East-West connection
                if c + 1 < n:
                    dsu.union(get_index(r, c, 1), get_index(r, c + 1, 3))

        return dsu.count
