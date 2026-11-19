from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r: int, c: int, visited: set) -> None:
            visited.add((r, c))
            curr_h = heights[r][c]
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in visited and heights[nr][nc] >= curr_h):
                    dfs(nr, nc, visited)
                    
        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)
            
        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)
            
        return [[r, c] for r, c in (pacific & atlantic)]
