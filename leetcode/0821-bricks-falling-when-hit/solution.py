class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        roof = m * n
        dsu = DSU(roof + 1)

        def node_id(r, c):
            return r * n + c

        # 1. Copy grid and apply all hits
        A = [row[:] for row in grid]
        for r, c in hits:
            A[r][c] -= 1

        # 2. Build DSU for the final state
        for r in range(m):
            for c in range(n):
                if A[r][c] == 1:
                    u = node_id(r, c)
                    if r == 0:
                        dsu.union(u, roof)
                    if r > 0 and A[r - 1][c] == 1:
                        dsu.union(u, node_id(r - 1, c))
                    if c > 0 and A[r][c - 1] == 1:
                        dsu.union(u, node_id(r, c - 1))

        # 3. Process hits in reverse
        res = [0] * len(hits)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]
            A[r][c] += 1

            # If it wasn't a brick originally, no bricks fall
            if A[r][c] != 1:
                continue

            prev_roof_size = dsu.get_size(roof)
            u = node_id(r, c)

            # Reconnect to neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and A[nr][nc] == 1:
                    dsu.union(u, node_id(nr, nc))

            # Connect to roof if it is on the top row
            if r == 0:
                dsu.union(u, roof)

            curr_roof_size = dsu.get_size(roof)
            # Fallen bricks = newly attached minus the brick itself
            res[i] = max(0, curr_roof_size - prev_roof_size - 1)

        return res
