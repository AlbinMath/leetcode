from collections import deque
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return True

        # Mapping: direction -> (dr, dc, opposite_direction)
        dirs = {
            'U': (-1, 0, 'D'),
            'D': (1, 0, 'U'),
            'L': (0, -1, 'R'),
            'R': (0, 1, 'L')
        }

        # Street openings for types 1 to 6
        openings = {
            1: ['L', 'R'],
            2: ['U', 'D'],
            3: ['L', 'D'],
            4: ['R', 'D'],
            5: ['L', 'U'],
            6: ['R', 'U']
        }

        queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while queue:
            r, c = queue.popleft()
            if r == m - 1 and c == n - 1:
                return True

            curr_type = grid[r][c]
            for d in openings[curr_type]:
                dr, dc, opp_d = dirs[d]
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    neighbor_type = grid[nr][nc]
                    # Check if neighbor opens toward the current cell
                    if opp_d in openings[neighbor_type]:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        return False
