import heapq

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # Base case: single cell requires 0 moves and 0 turns
        if m == 1 and n == 1:
            return grid[0][0]
        
        # Directions: 0: Up, 1: Down, 2: Left, 3: Right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # dist[r][c][d][t] stores the minimum cost to reach (r, c)
        # entering from direction d with t turns taken.
        # Initialized to infinity.
        INF = float('inf')
        dist = [[[[INF] * (k + 1) for _ in range(4)] for _ in range(n)] for _ in range(m)]
        
        pq = []
        
        # Push initial moves from (0, 0)
        # The first move does not count as a turn (turns = 0).
        for d, (dr, dc) in enumerate(dirs):
            nr, nc = dr, dc
            if 0 <= nr < m and 0 <= nc < n:
                cost = grid[0][0] + grid[nr][nc]
                dist[nr][nc][d][0] = cost
                heapq.heappush(pq, (cost, nr, nc, d, 0))
        
        while pq:
            cost, r, c, d, t = heapq.heappop(pq)
            
            # Reached target with optimal cost
            if r == m - 1 and c == n - 1:
                return cost
            
            if cost > dist[r][c][d][t]:
                continue
            
            for nd, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nt = t if nd == d else t + 1
                    
                    if nt <= k:
                        next_cost = cost + grid[nr][nc]
                        if next_cost < dist[nr][nc][nd][nt]:
                            dist[nr][nc][nd][nt] = next_cost
                            heapq.heappush(pq, (next_cost, nr, nc, nd, nt))
        
        return -1
