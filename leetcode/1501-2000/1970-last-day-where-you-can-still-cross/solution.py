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

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        total_cells = row * col
        top_virtual = total_cells
        bottom_virtual = total_cells + 1

        dsu = DSU(total_cells + 2)
        grid = [[0] * col for _ in range(row)]  # 0: water (in reverse), 1: land

        def node_id(r: int, c: int) -> int:
            return r * col + c

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Process cells backwards from the last day
        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day][0] - 1, cells[day][1] - 1
            grid[r][c] = 1
            curr_id = node_id(r, c)

            # Connect to top/bottom virtual nodes if on the edge rows
            if r == 0:
                dsu.union(curr_id, top_virtual)
            if r == row - 1:
                dsu.union(curr_id, bottom_virtual)

            # Union with adjacent land neighbors
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    dsu.union(curr_id, node_id(nr, nc))

            # The moment top and bottom connect, this is the last day we could cross
            if dsu.connected(top_virtual, bottom_virtual):
                return day

        return 0
