import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = sorted((arr, lv, idx) for idx, (arr, lv) in enumerate(times))
        
        available_chairs = []  # min-heap of freed chair numbers
        occupied_chairs = []   # min-heap of (leaving_time, chair_number)
        next_new_chair = 0
        
        for arrival, leaving, friend_id in events:
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                _, freed_chair = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, freed_chair)
            if available_chairs:
                chair = heapq.heappop(available_chairs)
            else:
                chair = next_new_chair
                next_new_chair += 1
                
            if friend_id == targetFriend:
                return chair
                
            heapq.heappush(occupied_chairs, (leaving, chair))
            
        return -1
