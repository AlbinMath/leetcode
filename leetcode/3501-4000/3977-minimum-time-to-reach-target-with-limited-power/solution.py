from typing import List
import heapq

class Solution:
    def minTimeMaxPower(
        self,
        n: int,
        edges: List[List[int]],
        power: int,
        cost: List[int],
        source: int,
        target: int
    ) -> List[int]:

        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))

        INF = float('inf')
        dist = [[INF] * (power + 1) for _ in range(n)]
        dist[source][power] = 0

        pq = [(0, source, power)]
        best_time = INF
        best_power = -1

        while pq:
            time, u, p = heapq.heappop(pq)

            if time > best_time:
                break

            if time != dist[u][p]:
                continue

            if u == target:
                best_time = time
                best_power = max(best_power, p)
                continue

            if p < cost[u]:
                continue

            remaining = p - cost[u]

            for v, t in graph[u]:
                new_time = time + t

                if new_time < dist[v][remaining]:
                    dist[v][remaining] = new_time
                    heapq.heappush(pq, (new_time, v, remaining))

        if best_power == -1:
            return [-1, -1]

        return [best_time, best_power]
