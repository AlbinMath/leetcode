import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        busy_rooms = []  # (end_time, room_index)
        counts = [0] * n
        
        for start, end in meetings:
            # Free up all rooms whose meetings have ended by `start`
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
                
            if free_rooms:
                room = heapq.heappop(free_rooms)
                counts[room] += 1
                heapq.heappush(busy_rooms, (end, room))
            else:
                earliest_end, room = heapq.heappop(busy_rooms)
                counts[room] += 1
                duration = end - start
                heapq.heappush(busy_rooms, (earliest_end + duration, room))
                
        max_meetings = max(counts)
        return counts.index(max_meetings)
