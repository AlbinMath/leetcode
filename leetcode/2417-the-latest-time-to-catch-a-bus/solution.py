from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        seen = set(passengers)

        j = 0
        cnt = 0
        for b in buses:
            cnt = 0
            while j < len(passengers) and passengers[j] <= b and cnt < capacity:
                j += 1
                cnt += 1

        cand = buses[-1] if cnt < capacity else passengers[j - 1]

        while cand in seen:
            cand -= 1
        return cand
