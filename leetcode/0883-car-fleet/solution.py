from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        lead_d, lead_s = 0, 1          # distance and speed of the fleet ahead
        for p, s in cars:
            d = target - p
            # Catches the fleet ahead iff d / s <= lead_d / lead_s
            if fleets and d * lead_s <= lead_d * s:
                continue
            fleets += 1
            lead_d, lead_s = d, s

        return fleets
