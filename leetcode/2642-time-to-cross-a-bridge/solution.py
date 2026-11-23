import heapq
from typing import List

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # Max-heaps (via negative values) ordered by least efficiency: (-(left + right), -index)
        left_wait = [(-(time[i][0] + time[i][2]), -i) for i in range(k)]
        heapq.heapify(left_wait)
        right_wait = []
        
        # Min-heaps ordered by completion time: (finish_time, index)
        left_work = []
        right_work = []
        
        curr_time = 0
        remaining_boxes = n
        
        while remaining_boxes > 0 or right_wait or right_work:
            # 1. Move any workers who finished working in either warehouse to their bridge queue
            while left_work and left_work[0][0] <= curr_time:
                _, i = heapq.heappop(left_work)
                heapq.heappush(left_wait, (-(time[i][0] + time[i][2]), -i))
                
            while right_work and right_work[0][0] <= curr_time:
                _, i = heapq.heappop(right_work)
                heapq.heappush(right_wait, (-(time[i][0] + time[i][2]), -i))
                
            # 2. Prioritize workers waiting on the right side to cross left
            if right_wait:
                _, neg_i = heapq.heappop(right_wait)
                i = -neg_i
                curr_time += time[i][2]  # left_i
                heapq.heappush(left_work, (curr_time + time[i][3], i))  # + put_i
                
            # 3. Otherwise, send a worker from the left if boxes still need to be picked up
            elif remaining_boxes > 0 and left_wait:
                _, neg_i = heapq.heappop(left_wait)
                i = -neg_i
                remaining_boxes -= 1
                curr_time += time[i][0]  # right_i
                heapq.heappush(right_work, (curr_time + time[i][1], i))  # + pick_i
                
            # 4. Bridge is idle; jump clock to the earliest warehouse completion event
            else:
                next_time = float('inf')
                if remaining_boxes > 0 and left_work:
                    next_time = min(next_time, left_work[0][0])
                if right_work:
                    next_time = min(next_time, right_work[0][0])
                curr_time = next_time
                
        return curr_time
