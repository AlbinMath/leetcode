from typing import List

class Solution:
    def nearestDrone(self, drones: List[List[int]], target: List[int]) -> int:
        tx, ty = target
        best_idx = -1
        best_dist = float('inf')
        for i, (x, y, r) in enumerate(drones):
            d = abs(x - tx) + abs(y - ty)
            if d <= r and d < best_dist:
                best_dist = d
                best_idx = i
        return best_idx
