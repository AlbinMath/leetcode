from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total_boomerangs = 0
        
        for x1, y1 in points:
            dist_counts = defaultdict(int)
            
            # Count how many points share each squared distance from (x1, y1)
            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                dist_sq = dx * dx + dy * dy
                dist_counts[dist_sq] += 1
            
            # For each group of m equidistant points, add m * (m - 1) permutations
            for count in dist_counts.values():
                if count > 1:
                    total_boomerangs += count * (count - 1)
                    
        return total_boomerangs
