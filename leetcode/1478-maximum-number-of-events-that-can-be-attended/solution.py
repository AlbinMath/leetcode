import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        heap = []  # end days of events available today
        i = 0
        day = 0
        count = 0
        while i < n or heap:
            if not heap:
                day = max(day, events[i][0])  # skip idle days
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)  # expired
            if heap:
                heapq.heappop(heap)  # attend the earliest-ending event
                count += 1
            day += 1
        return count
