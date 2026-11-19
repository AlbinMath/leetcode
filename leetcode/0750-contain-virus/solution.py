from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        total_walls = 0

        while True:
            visited = set()
            regions = []    # list of infected cell sets/lists
            frontiers = []  # list of unique threatened (r, c) sets
            walls_list = [] # list of perimeter wall counts

            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and (r, c) not in visited:
                        cells = []
                        frontier = set()
                        walls = 0
                        stack = [(r, c)]
                        visited.add((r, c))

                        while stack:
                            cr, cc = stack.pop()
                            cells.append((cr, cc))
                            for dr, dc in dirs:
                                nr, nc = cr + dr, cc + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 0:
                                        walls += 1
                                        frontier.add((nr, nc))
                                    elif isInfected[nr][nc] == 1 and (nr, nc) not in visited:
                                        visited.add((nr, nc))
                                        stack.append((nr, nc))

                        regions.append(cells)
                        frontiers.append(frontier)
                        walls_list.append(walls)

            if not regions:
                break

            best_idx = max(range(len(regions)), key=lambda i: len(frontiers[i]))
            if not frontiers[best_idx]:
                break

            total_walls += walls_list[best_idx]
            for r, c in regions[best_idx]:
                isInfected[r][c] = 2

            for i, frontier in enumerate(frontiers):
                if i != best_idx:
                    for r, c in frontier:
                        isInfected[r][c] = 1

        return total_walls
