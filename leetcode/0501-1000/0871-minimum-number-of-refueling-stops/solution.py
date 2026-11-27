import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap = []  # max-heap via negated fuel
        fuel = startFuel  # farthest position reachable so far
        stops = 0
        for pos, gas in stations + [[target, 0]]:
            while fuel < pos:
                if not heap:
                    return -1
                fuel += -heapq.heappop(heap)
                stops += 1
            heapq.heappush(heap, -gas)
        return stops
