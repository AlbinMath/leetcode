import heapq

class Solution:
    def minCost(self, m: int, n: int, penalty: list[list[int]]) -> int:
        # Entrance cost function
        def enter_cost(r: int, c: int) -> int:
            return (r + 1) * (c + 1)

        # dist[r][c][p] stores the minimum cost to reach (r, c)
        # where the next action will have parity p (1 = odd, 0 = even).
        # We can flatten (r, c, p) to 2 * (r * n + c) + p
        num_cells = m * n
        INF = float('inf')
        dist = [INF] * (2 * num_cells)

        start_cost = enter_cost(0, 0)
        # Initially at (0, 0) before action 1 (odd parity -> p = 1)
        start_idx = 2 * 0 + 1
        dist[start_idx] = start_cost

        # Priority queue stores (cost, r, c, p)
        pq = [(start_cost, 0, 0, 1)]

        # Directions: (dr, dc, is_odd_friendly)
        # Right (0, 1) and Down (1, 0) are odd-friendly (p = 1)
        # Left (0, -1) and Up (-1, 0) are even-friendly (p = 0)
        moves = [
            (0, 1, 1),
            (1, 0, 1),
            (0, -1, 0),
            (-1, 0, 0)
        ]

        while pq:
            d, r, c, p = heapq.heappop(pq)

            idx = 2 * (r * n + c) + p
            if d > dist[idx]:
                continue

            # If we reached the target cell, this is the optimal cost
            if r == m - 1 and c == n - 1:
                return d

            next_p = 1 - p
            pen = penalty[r][c]

            # Option 1: Wait at current cell
            wait_cost = d + pen
            wait_idx = 2 * (r * n + c) + next_p
            if wait_cost < dist[wait_idx]:
                dist[wait_idx] = wait_cost
                heapq.heappush(pq, (wait_cost, r, c, next_p))

            # Option 2: Move to adjacent cells
            for dr, dc, move_parity in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    extra = 0 if move_parity == p else pen
                    move_cost = d + enter_cost(nr, nc) + extra
                    next_idx = 2 * (nr * n + nc) + next_p

                    if move_cost < dist[next_idx]:
                        dist[next_idx] = move_cost
                        heapq.heappush(pq, (move_cost, nr, nc, next_p))

        return -1
