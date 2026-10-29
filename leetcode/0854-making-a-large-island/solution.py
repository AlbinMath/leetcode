class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        area = {}
        
        # 1. Label each island and compute its size
        def dfs(r, c, label):
            count = 1
            grid[r][c] = label
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    count += dfs(nr, nc, label)
            return count

        max_area = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size = dfs(r, c, island_id)
                    area[island_id] = size
                    max_area = max(max_area, size)
                    island_id += 1
                    
        # If the entire grid is already all 1s
        if max_area == n * n:
            return n * n

        # 2. Try flipping each 0 to 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen_islands = set()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen_islands.add(grid[nr][nc])
                    
                    combined = 1 + sum(area[i_id] for i_id in seen_islands)
                    max_area = max(max_area, combined)
                    
        return max_area
