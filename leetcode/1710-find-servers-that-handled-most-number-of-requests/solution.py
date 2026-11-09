import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = list(range(k))          # heap of virtual indices (already a valid heap)
        busy = []                      # heap of (end_time, server_id)
        count = [0] * k

        for i, (start, dur) in enumerate(zip(arrival, load)):
            # Release servers that have finished by time `start`.
            while busy and busy[0][0] <= start:
                _, sid = heapq.heappop(busy)
                # Smallest value >= i that is congruent to sid (mod k)
                nxt = i + ((sid - i) % k)
                heapq.heappush(free, nxt)

            if not free:
                continue               # all servers busy -> drop

            sid = heapq.heappop(free) % k
            count[sid] += 1
            heapq.heappush(busy, (start + dur, sid))

        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]
