from typing import List
import heapq

class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        empty_graph = [[] for _ in range(n)]
        loaded_graph = [[] for _ in range(n)]

        for u, v, cost, taxi in roads:
            empty_graph[u].append((v, cost))
            empty_graph[v].append((u, cost))

            loaded_graph[u].append((v, cost * taxi))
            loaded_graph[v].append((u, cost * taxi))

        INF = float('inf')

        def dijkstra(graph, src):
            dist = [INF] * n
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                d, u = heapq.heappop(pq)

                if d != dist[u]:
                    continue

                for v, w in graph[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))

            return dist

        # Empty-trip distances from each starting shop.
        empty_dist = [dijkstra(empty_graph, i) for i in range(n)]

        # Return-trip distances to each starting shop.
        # The loaded graph is undirected, so these distances are symmetric.
        loaded_dist = [dijkstra(loaded_graph, i) for i in range(n)]

        ans = []

        for i in range(n):
            best = prices[i]

            for j in range(n):
                total = empty_dist[i][j] + prices[j] + loaded_dist[j][i]
                best = min(best, total)

            ans.append(best)

        return ans
