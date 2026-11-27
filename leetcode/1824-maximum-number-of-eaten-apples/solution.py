import heapq
from typing import List

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        heap = []  # [expiry_day, count]
        eaten = 0
        i = 0
        while i < n or heap:
            if i < n and apples[i] > 0:
                heapq.heappush(heap, [i + days[i], apples[i]])
            while heap and heap[0][0] <= i:
                heapq.heappop(heap)
            if heap:
                heap[0][1] -= 1
                eaten += 1
                if heap[0][1] == 0:
                    heapq.heappop(heap)
            i += 1
        return eaten
