from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if forest[0][0] == 0:
            return -1
            
        m, n = len(forest), len(forest[0])
        trees = sorted(
            (forest[r][c], r, c)
            for r in range(m)
            for c in range(n)
            if forest[r][c] > 1
        )
        
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        def bfs(sr: int, sc: int, tr: int, tc: int) -> int:
            if sr == tr and sc == tc:
                return 0
            queue = deque([(sr, sc, 0)])
            visited = {(sr, sc)}
            while queue:
                r, c, steps = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] > 0 and (nr, nc) not in visited:
                        if nr == tr and nc == tc:
                            return steps + 1
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
            return -1
            
        curr_r, curr_c = 0, 0
        total_steps = 0
        for _, tr, tc in trees:
            dist = bfs(curr_r, curr_c, tr, tc)
            if dist == -1:
                return -1
            total_steps += dist
            curr_r, curr_c = tr, tc
            
        return total_steps
